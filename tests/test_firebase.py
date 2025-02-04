import pytest
from firebase_admin import credentials, initialize_app, firestore
import os
import json
from dotenv import load_dotenv

load_dotenv()

def setup_firebase():
    """Initialize Firebase with service account"""
    try:
        # Get service account JSON from environment variable
        service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")
        if not service_account_json:
            pytest.skip("Firebase service account not configured")
        
        # Parse the JSON string into a dictionary
        service_account_dict = json.loads(service_account_json)
        
        # Initialize Firebase with the credentials
        cred = credentials.Certificate(service_account_dict)
        initialize_app(cred)
        return firestore.client()
    except Exception as e:
        pytest.skip(f"Failed to initialize Firebase: {str(e)}")

# Initialize Firebase client
db = setup_firebase()

def test_firebase_connection():
    """Test Firebase connection"""
    try:
        # Try to access a collection
        db.collection('tasks').limit(1).get()
        assert True
    except Exception as e:
        pytest.fail(f"Firebase connection failed: {str(e)}")

def test_task_creation():
    """Test task creation in Firebase"""
    test_task = {
        'title': 'Test Task',
        'description': 'Test Description',
        'assignedTo': 'Test User',
        'priority': 'medium',
        'status': 'pending'
    }
    
    try:
        # Add test task
        doc_ref = db.collection('tasks').add(test_task)
        assert doc_ref[1].id is not None
        
        # Clean up - delete test task
        db.collection('tasks').document(doc_ref[1].id).delete()
    except Exception as e:
        pytest.fail(f"Task creation test failed: {str(e)}")