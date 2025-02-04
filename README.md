# Family Task Manager

A modern family task management application with AI-assisted features - a full-stack web application.

## Technical Highlights

### Frontend Technologies
- **React 18**: Building user interfaces with the latest React features
- **TypeScript**: Type safety and enhanced development experience
- **Tailwind CSS**: Responsive and modern UI design
- **Vite**: Fast development build tool
- **Component Libraries**: 
  - @headlessui/react: Unstyled, fully accessible UI components
  - @heroicons/react: SVG icon collection

### Backend Integration
- **Firebase**: 
  - Authentication: User authentication system
  - Firestore: Real-time database
  - Firebase Admin SDK: Backend service integration

### AI Integration
- **DeepSeek API**: Intelligent task suggestion generation
- Natural Language Processing: Converting user input into structured task suggestions

### Testing Framework
- **Frontend Testing**:
  - Vitest: Unit testing framework
  - React Testing Library: Component testing
  - Test coverage reporting

- **Backend Testing**:
  - Pytest: Python testing framework
  - Integration Tests: Firebase and DeepSeek API
  - Github Actions: Automated testing workflow

## Core Features

### 1. User Authentication
- Email and password login/registration
- User session management
- Secure authentication flow

### 2. Task Management
- Create, Read, Update, Delete tasks
- Task priority management
- Task assignment functionality
- Due date tracking

### 3. AI Assistance
- Intelligent task suggestion generation
- Natural language processing
- Real-time suggestion updates

### 4. Real-time Synchronization
- Firestore real-time database integration
- Multi-user real-time updates
- Data consistency guarantee

## Project Highlights

### 1. Modern Architecture
- Component-based design
- TypeScript type safety
- Responsive design

### 2. Performance Optimization
- Vite fast building
- Code splitting
- Lazy-loaded components

### 3. User Experience
- Intuitive interface design
- Real-time feedback
- AI assistance

### 4. Code Quality
- ESLint code standards
- Complete test coverage
- CI/CD integration

## Development Practices

### 1. Version Control
- Git workflow
- Branch management
- Code review process

### 2. Test-Driven Development
- Unit testing
- Integration testing
- End-to-end testing

### 3. Continuous Integration
- Github Actions workflow
- Automated testing
- Code coverage reporting

## Getting Started

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm run test

# Build for production
npm run build
```

## Environment Configuration

Create a `.env` file and configure the following environment variables:

```env
# Firebase Configuration
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_FIREBASE_MEASUREMENT_ID=your_measurement_id

# DeepSeek API Configuration
DEEPSEEK_API_KEY=your_api_key

# Firebase Admin SDK
FIREBASE_SERVICE_ACCOUNT=path_to_service_account.json
```

## Testing

### Frontend Tests
```bash
npm run test
```

### Backend Tests
1. source venv/bin/activate
2. pip3 install -r requirements.txt
3. python3 -m pytest tests/ --cov=./

