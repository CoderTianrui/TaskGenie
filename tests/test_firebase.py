import pytest
from firebase_admin import credentials, initialize_app, firestore
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase Admin SDK for testing
cred = credentials.Certificate(os.getenv("FIREBASE_SERVICE_ACCOUNT"))
initialize_app(cred)
db = firestore.client()

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