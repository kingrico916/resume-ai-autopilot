# CLAUDE.md - AI Assistant Guide for Resume AI Autopilot

**Last Updated**: 2025-11-18
**Project**: Resume AI Autopilot
**Repository**: kingrico916/resume-ai-autopilot

## Project Overview

Resume AI Autopilot is an AI-powered application designed to automate and optimize resume-related tasks. This could include resume generation, optimization, parsing, matching, or automated job application processes.

### Current State
- **Status**: New/Greenfield Project
- **Primary Branch**: TBD (to be determined)
- **Active Development Branch**: claude/claude-md-mi46mj2bhio7rg97-01UcRu5oM1d3yUPjvnn4BR1F

## Project Architecture

### Anticipated Tech Stack
Based on common AI resume processing applications, this project likely uses:

- **Language**: Python, TypeScript/Node.js, or both
- **AI/ML**: OpenAI API, Anthropic Claude API, or similar LLM integration
- **Framework**: Express.js, FastAPI, or Flask
- **Database**: PostgreSQL, MongoDB, or SQLite for data persistence
- **Frontend**: React, Next.js, or Vue.js (if applicable)
- **Testing**: Jest, pytest, or similar
- **Deployment**: Docker, Cloud Platform (AWS, GCP, Azure)

### Expected Directory Structure

```
resume-ai-autopilot/
├── .github/              # GitHub workflows and templates
│   └── workflows/        # CI/CD pipeline definitions
├── src/                  # Source code
│   ├── api/             # API endpoints and routes
│   ├── services/        # Business logic and AI integration
│   ├── models/          # Data models and schemas
│   ├── utils/           # Utility functions
│   └── config/          # Configuration files
├── tests/               # Test files
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── e2e/             # End-to-end tests
├── docs/                # Documentation
├── scripts/             # Build and deployment scripts
├── data/                # Sample data, templates, or training data
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore file
├── package.json         # Node.js dependencies (if applicable)
├── requirements.txt     # Python dependencies (if applicable)
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker compose for local development
├── README.md            # Project documentation
└── CLAUDE.md            # This file - AI assistant guide
```

## Development Workflow

### Git Workflow

1. **Branch Naming Convention**
   - Feature branches: `feature/<descriptive-name>`
   - Bug fixes: `fix/<issue-description>`
   - Claude AI branches: `claude/<session-id>`
   - Hotfixes: `hotfix/<issue-description>`

2. **Commit Messages**
   - Use conventional commits format
   - Format: `type(scope): description`
   - Types: feat, fix, docs, style, refactor, test, chore
   - Example: `feat(resume-parser): add PDF parsing support`

3. **Pull Request Process**
   - Create descriptive PR titles and descriptions
   - Include testing steps and verification methods
   - Reference related issues
   - Ensure all tests pass before requesting review

### Code Quality Standards

1. **Linting and Formatting**
   - Use ESLint/Prettier for JavaScript/TypeScript
   - Use Black/Flake8 for Python
   - Run linters before committing

2. **Testing Requirements**
   - Minimum 80% code coverage for new features
   - Write unit tests for all business logic
   - Include integration tests for API endpoints
   - Add e2e tests for critical user workflows

3. **Documentation**
   - Document all public APIs
   - Include JSDoc/docstrings for functions
   - Update README.md when adding features
   - Maintain API documentation (OpenAPI/Swagger)

## AI Assistant Guidelines

### When Working on This Project

1. **Always Check Before Creating**
   - Search for existing implementations before creating new ones
   - Check if utilities or helpers already exist
   - Review existing patterns and follow them

2. **File Operations**
   - Prefer editing existing files over creating new ones
   - Read files before modifying them
   - Maintain consistent code style with existing code

3. **Security Considerations**
   - Never commit API keys, secrets, or credentials
   - Use environment variables for sensitive data
   - Validate and sanitize all user inputs
   - Implement rate limiting for API endpoints
   - Follow OWASP security guidelines
   - Be cautious with file uploads and parsing

4. **API Integration Best Practices**
   - Implement proper error handling for AI API calls
   - Add retry logic with exponential backoff
   - Monitor API usage and costs
   - Cache responses when appropriate
   - Handle rate limits gracefully

5. **Resume Processing Specifics**
   - Respect user privacy and data protection laws (GDPR, CCPA)
   - Implement data anonymization where needed
   - Handle PII (Personally Identifiable Information) securely
   - Support multiple resume formats (PDF, DOCX, TXT)
   - Validate extracted data for accuracy

### Task Management

When working on tasks:

1. **Use TodoWrite Tool** for complex multi-step tasks
2. **Break Down Large Tasks** into smaller, manageable steps
3. **Mark Progress** as you complete each step
4. **Test Incrementally** after each significant change

### Common Tasks and Patterns

#### Adding a New Feature

1. Understand requirements and existing codebase
2. Design the feature architecture
3. Implement core functionality
4. Add comprehensive tests
5. Update documentation
6. Create pull request with detailed description

#### Debugging Issues

1. Reproduce the issue
2. Add logging/debugging statements
3. Identify root cause
4. Implement fix
5. Add regression tests
6. Verify fix works

#### Refactoring Code

1. Ensure existing tests pass
2. Make incremental changes
3. Run tests after each change
4. Update documentation if needed
5. Commit frequently with clear messages

## Key Technical Considerations

### Resume Processing Pipeline

Expected components:

1. **Input Handler**
   - Accept multiple file formats
   - Validate file integrity
   - Extract text content

2. **Parser/Extractor**
   - Use AI to extract structured data
   - Identify sections (education, experience, skills)
   - Parse dates, locations, and other entities

3. **Optimizer**
   - Analyze resume content
   - Suggest improvements
   - Match against job descriptions
   - Generate tailored versions

4. **Output Generator**
   - Format results
   - Generate reports or optimized resumes
   - Export in various formats

### AI Integration Patterns

```python
# Example pattern for AI calls with error handling
async def process_with_ai(content, retry_count=3):
    """Process content using AI with retry logic."""
    for attempt in range(retry_count):
        try:
            response = await ai_client.generate(
                prompt=build_prompt(content),
                max_tokens=1000,
                temperature=0.7
            )
            return parse_response(response)
        except RateLimitError:
            if attempt < retry_count - 1:
                await asyncio.sleep(2 ** attempt)
            else:
                raise
        except APIError as e:
            logger.error(f"AI API error: {e}")
            raise
```

### Environment Variables

Expected environment variables:

```bash
# AI Service Configuration
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
AI_MODEL=gpt-4  # or claude-3-opus-20240229

# Application Configuration
NODE_ENV=development
PORT=3000
LOG_LEVEL=info

# Database Configuration
DATABASE_URL=
REDIS_URL=

# Security
JWT_SECRET=
ENCRYPTION_KEY=

# File Storage
UPLOAD_DIR=./uploads
MAX_FILE_SIZE=10485760  # 10MB

# Rate Limiting
RATE_LIMIT_WINDOW=900000  # 15 minutes
RATE_LIMIT_MAX_REQUESTS=100
```

## Performance Optimization

1. **Caching Strategy**
   - Cache AI responses for identical inputs
   - Use Redis for session management
   - Implement response compression

2. **Async Processing**
   - Use job queues for long-running tasks
   - Implement background workers
   - Provide status updates to users

3. **Resource Management**
   - Limit concurrent AI API calls
   - Implement request throttling
   - Monitor memory usage for large files

## Testing Guidelines

### Unit Tests
- Test individual functions and methods
- Mock external dependencies (AI APIs, databases)
- Aim for 100% coverage of business logic

### Integration Tests
- Test API endpoints
- Verify database operations
- Test AI integration flows

### E2E Tests
- Test complete user workflows
- Verify UI interactions (if applicable)
- Test with real-world resume samples

## Deployment Considerations

1. **Environment Setup**
   - Use Docker for consistent environments
   - Implement CI/CD pipelines
   - Automate testing and deployment

2. **Monitoring**
   - Log all errors and warnings
   - Track AI API usage and costs
   - Monitor application performance
   - Set up alerts for critical issues

3. **Scalability**
   - Design for horizontal scaling
   - Use load balancers
   - Implement caching layers
   - Consider serverless options for sporadic workloads

## Common Pitfalls to Avoid

1. **Don't hardcode credentials** - Always use environment variables
2. **Don't skip input validation** - Validate all user inputs
3. **Don't ignore error handling** - Implement comprehensive error handling
4. **Don't forget about costs** - Monitor and optimize AI API usage
5. **Don't store raw PII** - Encrypt sensitive data at rest and in transit
6. **Don't skip documentation** - Keep docs up-to-date with code changes
7. **Don't commit large files** - Use .gitignore appropriately
8. **Don't make assumptions** - Verify understanding before implementing

## Resources and References

### Documentation
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API Documentation](https://docs.anthropic.com)
- [Resume Parser Best Practices](https://example.com)

### Tools
- **PDF Processing**: PyPDF2, pdf-parse, pdfplumber
- **DOCX Processing**: python-docx, mammoth
- **NLP**: spaCy, NLTK
- **Testing**: Jest, pytest, Supertest
- **API Documentation**: Swagger/OpenAPI

## Questions for Clarification

When starting new features, consider asking:

1. What is the primary use case for this feature?
2. What resume formats need to be supported?
3. What AI models should be used and why?
4. What are the performance requirements?
5. What are the privacy and security requirements?
6. How should errors be communicated to users?
7. What metrics should be tracked?

## Contributing

As an AI assistant working on this project:

1. **Understand before implementing** - Ask questions if requirements are unclear
2. **Follow established patterns** - Maintain consistency with existing code
3. **Test thoroughly** - Ensure changes don't break existing functionality
4. **Document your changes** - Update relevant documentation
5. **Communicate clearly** - Provide clear commit messages and PR descriptions

## Next Steps for Initial Setup

If this is a new project, consider these initial tasks:

1. **Initialize Project Structure**
   - Create directory structure
   - Set up package.json or requirements.txt
   - Configure linting and formatting tools

2. **Set Up Development Environment**
   - Create .env.example file
   - Set up Docker configuration
   - Configure git hooks (pre-commit, pre-push)

3. **Implement Core Components**
   - Basic server setup
   - Database connection
   - AI API integration
   - File upload handling

4. **Set Up Testing Framework**
   - Configure test runners
   - Create sample tests
   - Set up coverage reporting

5. **Documentation**
   - Create comprehensive README.md
   - Set up API documentation
   - Create contribution guidelines

---

**Note for AI Assistants**: This document should be updated as the project evolves. Keep it synchronized with the actual codebase structure and conventions. When you make significant architectural changes, update this file accordingly.
