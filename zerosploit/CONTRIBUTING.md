# Contributing to ZeroSploit

Thank you for your interest in contributing to ZeroSploit! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our ethical guidelines:

- **Only use ZeroSploit for authorized security testing**
- **Respect the privacy and security of others**
- **Follow responsible disclosure practices**
- **Contribute to the security community positively**

## How to Contribute

### Reporting Issues

When reporting issues, please include:

1. **Clear description** of the problem
2. **Steps to reproduce** the issue
3. **Expected behavior** vs actual behavior
4. **Environment information** (OS, Python version, etc.)
5. **Error messages** or logs (if applicable)

### Suggesting Features

When suggesting new features:

1. **Check existing issues** to avoid duplicates
2. **Describe the use case** for the feature
3. **Explain the benefits** to the project
4. **Consider security implications**
5. **Provide examples** if applicable

### Code Contributions

#### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/zerosploit.git
   cd zerosploit
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Install development dependencies:
   ```bash
   pip install pytest black flake8 mypy
   ```

#### Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our coding standards
3. Add tests for new functionality
4. Update documentation as needed
5. Run tests to ensure nothing breaks:
   ```bash
   python -m pytest tests/
   ```

#### Coding Standards

- **PEP 8**: Follow Python style guidelines
- **Type hints**: Use type hints where appropriate
- **Docstrings**: Add docstrings to all functions and classes
- **Comments**: Add comments for complex logic
- **Security**: Always consider security implications

#### Testing

- Write unit tests for new functionality
- Update existing tests when modifying code
- Ensure all tests pass before submitting
- Test on multiple Python versions if possible

#### Security Considerations

When contributing code:

1. **Never include actual exploits** - keep examples educational
2. **Add appropriate warnings** for potentially dangerous functionality
3. **Validate all inputs** to prevent misuse
4. **Follow ethical guidelines** in all contributions
5. **Consider legal implications** of new features

### Documentation

Good documentation helps everyone:

- **API documentation** for new functions
- **Usage examples** for new features
- **Security warnings** where appropriate
- **Installation instructions** for new dependencies

### Pull Request Process

1. **Update documentation** for any new features
2. **Add tests** for new functionality
3. **Update CHANGELOG.md** with your changes
4. **Ensure tests pass** and code follows style guidelines
5. **Write clear commit messages**

#### Pull Request Template

```
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Security Impact
- [ ] No security implications
- [ ] Security implications considered and addressed
- [ ] Ethical guidelines followed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

### Release Process

For maintainers:

1. Update version numbers
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Update documentation

## Getting Help

If you need help:

1. Check existing documentation
2. Search existing issues
3. Ask questions in discussions
4. Contact maintainers

## Recognition

Contributors will be recognized in:

- CHANGELOG.md
- README.md contributors section
- Release notes (for significant contributions)

## Legal Considerations

By contributing to ZeroSploit:

1. You agree to license your contributions under the MIT License
2. You confirm your contributions are your original work
3. You understand the ethical implications of the project
4. You agree to follow responsible disclosure practices

## Areas for Contribution

We welcome contributions in these areas:

### Code
- Bug fixes
- New features
- Performance improvements
- Security enhancements

### Documentation
- API documentation
- Usage examples
- Security guidelines
- Installation guides

### Testing
- Unit tests
- Integration tests
- Performance tests
- Security tests

### Security Research
- Vulnerability identification
- Security best practices
- Ethical guidelines
- Legal considerations

## Disclaimer

Contributors must understand that:

- This tool is for authorized security testing only
- Misuse of this tool may be illegal
- Contributors are responsible for their contributions
- The project maintains ethical standards

Thank you for contributing to ZeroSploit and helping improve security for everyone!