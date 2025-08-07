# Course Generation and Recommendation Platform

Welcome to the **Course Generation and Recommendation Platform**, an educational system designed to create personalized learning experiences for students. Built with a modular and flexible architecture inspired by platforms like Shopware, this project provides tools for assessing student knowledge, recommending learning paths, tracking performance, and facilitating interactive learning.

## Repository
[https://github.com/victordeman/Course-Generation-and-Recommendation-Platform](https://github.com/victordeman/Course-Generation-and-Recommendation-Platform)

## Features

1. **Interactive Quizzes**:
   - Assess students' knowledge levels through dynamic quizzes.
   - Results feed into the recommendation engine to tailor learning paths.

2. **Learning Path Recommendation**:
   - Generates personalized course sequences based on quiz performance.
   - Ensures content matches the student's current knowledge level.

3. **Grade Tracking System**:
   - Tracks student performance on assignments.
   - Provides recommendations for improvement based on grades.

4. **Event Listeners for Activity Tracking**:
   - Monitors clicks, scrolls, hovers, and other interactions.
   - Analyzes engagement to refine learning recommendations.

5. **Chat System with Retrieval Augmented Generation (RAG)**:
   - Enables real-time interaction with course content.
   - Uses RAG to provide contextual answers based on course materials.

## Tech Stack

- **Back-End**:
  - PHP, Symfony (core application logic)
  - Python (for scripting, recommendation engine, and Streamlit interface)
- **Front-End**:
  - Vue.js, TypeScript (interactive UI components)
  - Twig, HTML, CSS, JavaScript (ES6), Bootstrap (responsive design)
- **Database**:
  - MySQL or MongoDB (for storing student data, quiz results, and grades)
- **Tools**:
  - PHP Storm (IDE)
  - Git (version control)
  - Jira (project management)
  - Confluence (documentation)
- **Optional**:
  - RabbitMQ (message queuing)
  - Node.js (additional scripting)

## Repository Structure

```
$PROJECT_NAME/
├── backend/
│   ├── php/                    # PHP core logic
│   ├── symfony/                # Symfony framework components
│   ├── python/                 # Python scripts (e.g., recommendation engine)
├── frontend/
│   ├── vue/                    # Vue.js components
│   ├── twig/                   # Twig templates
│   ├── static/
│   │   ├── css/               # CSS styles
│   │   ├── js/                # JavaScript files
│   │   ├── images/            # Static assets
├── streamlit/                  # Streamlit interface for visualization
├── database/
│   ├── migrations/             # Database migrations
│   ├── seeds/                 # Database seed data
├── config/                     # Configuration files (e.g., Symfony config)
├── tests/
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
├── tools/
│   ├── scripts/               # Utility scripts
│   ├── docs/                  # Documentation
├── optional/
│   ├── rabbitmq/              # RabbitMQ configurations
│   ├── nodejs/                # Node.js scripts
├── README.md                  # Project documentation
```

## Getting Started

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/victordeman/Course-Generation-and-Recommendation-Platform
   \`\`\`
2. Set up the environment (manually install dependencies):
   - PHP/Symfony for backend
   - Node.js/NPM for Vue.js and Bootstrap
   - Python/Streamlit for the interface
   - MySQL/MongoDB for the database
3. Configure the application using `config/config.yaml`.
4. Run migrations from `database/migrations/`.
5. Start the Streamlit interface: `streamlit run streamlit/app.py`.
6. Access the frontend via the provided URLs after setup.

## Development Workflow

- Use **PHP Storm** for coding and debugging.
- Track tasks with **Jira**.
- Document processes in **Confluence**.
- Test with **PHPUnit** (PHP) and **unittest** (Python).

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

