# 🤝 Contributing to Flood Detection Project

Thank you for your interest in contributing to the Flood Detection Using Deep Learning project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## 🤗 Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background or experience level.

### Expected Behavior
- Be respectful and considerate
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what's best for the project and community

### Unacceptable Behavior
- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Other conduct which could be considered inappropriate

## 💡 How Can I Contribute?

### 1. Reporting Bugs
Found a bug? Please create an issue with:
- **Clear title**: Brief description of the problem
- **Steps to reproduce**: Detailed steps to recreate the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, browser
- **Screenshots**: If applicable
- **Error logs**: Copy relevant error messages

**Template:**
```markdown
**Bug Description**
Brief description

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Environment**
- OS: [e.g., Windows 10, Ubuntu 20.04]
- Python: [e.g., 3.9.5]
- Browser: [e.g., Chrome 91]
```

### 2. Suggesting Enhancements
Have an idea? Create an issue with:
- **Clear title**: Brief description of enhancement
- **Motivation**: Why this would be useful
- **Proposed solution**: How it could be implemented
- **Alternatives**: Other approaches considered
- **Additional context**: Screenshots, mockups, examples

### 3. Improving Documentation
Documentation contributions are highly valued! You can:
- Fix typos or unclear explanations
- Add code examples
- Improve installation instructions
- Create tutorials or guides
- Translate documentation

### 4. Writing Code
Code contributions can include:
- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Test coverage improvements

## 🚀 Getting Started

### 1. Fork the Repository
Click the "Fork" button on GitHub to create your copy.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR-USERNAME/Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-.git
cd Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-
```

### 3. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if any)
pip install pytest flake8 black
```

### 4. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding tests

## 🔧 Development Workflow

### 1. Make Your Changes
- Write clean, readable code
- Follow existing code style
- Add comments where necessary
- Update documentation as needed

### 2. Test Your Changes
```bash
# Run the application
python app.py

# Test manually in browser
# Try different images and scenarios

# Run unit tests (if available)
pytest

# Check code style
flake8 app.py
```

### 3. Commit Your Changes
```bash
git add .
git commit -m "feat: add new feature description"
```

**Commit message conventions:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

**Example commit messages:**
```bash
git commit -m "feat: add batch processing capability"
git commit -m "fix: resolve image upload error on Windows"
git commit -m "docs: update installation instructions"
git commit -m "refactor: improve preprocessing pipeline"
```

### 4. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 5. Create Pull Request
1. Go to your fork on GitHub
2. Click "Pull Request" button
3. Fill out the PR template
4. Wait for review

## 📝 Coding Standards

### Python Style Guide
We follow PEP 8 with some flexibility.

#### Key Points:
- **Indentation**: 4 spaces (no tabs)
- **Line length**: Max 100 characters (soft limit)
- **Imports**: Group into stdlib, third-party, local
- **Naming**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

#### Example:
```python
"""
Module docstring explaining purpose.
"""

# Standard library imports
import os
import sys

# Third-party imports
import numpy as np
import tensorflow as tf

# Local imports
from app import preprocess_image


class ImageProcessor:
    """Class docstring."""
    
    MAX_FILE_SIZE = 10485760  # 10MB
    
    def __init__(self, model_path):
        """Initialize with model path."""
        self.model_path = model_path
        
    def process_image(self, image_path):
        """
        Process a single image.
        
        Args:
            image_path (str): Path to image file
            
        Returns:
            np.ndarray: Processed image array
        """
        # Implementation
        pass
```

### Documentation Standards

#### Docstrings
Use Google-style docstrings:

```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Longer description if needed. Explain what the function does,
    any important details, edge cases, etc.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        return_type: Description of return value
        
    Raises:
        ExceptionType: When this exception occurs
        
    Example:
        >>> result = function_name(arg1, arg2)
        >>> print(result)
        Expected output
    """
```

#### Comments
- Use comments to explain **why**, not **what**
- Keep comments up-to-date with code changes
- Avoid obvious comments

**Good:**
```python
# Apply sigmoid threshold for binary classification
prediction = "Flooded" if probability >= 0.5 else "Non-Flooded"
```

**Avoid:**
```python
# Set x to 5
x = 5
```

### Frontend Standards (HTML/JavaScript)

#### HTML
- Use semantic HTML5 tags
- Indent with 2 spaces
- Include alt text for images

#### JavaScript
- Use meaningful variable names
- Add comments for complex logic
- Handle errors gracefully

#### CSS
- Use consistent indentation
- Group related properties
- Add comments for sections

## 🧪 Testing Guidelines

### Manual Testing Checklist
Before submitting a PR, test:

- [ ] Application starts without errors
- [ ] Home page loads correctly
- [ ] Image upload works
- [ ] Image preview displays
- [ ] Predictions return results
- [ ] Error handling works
- [ ] UI is responsive
- [ ] Works in different browsers
- [ ] No console errors

### Writing Tests (Future)
When adding tests:
```python
def test_preprocess_image():
    """Test image preprocessing pipeline."""
    # Arrange
    test_image_path = "test_images/sample.jpg"
    
    # Act
    result = preprocess_image(test_image_path)
    
    # Assert
    assert result.shape == (1, 128, 128, 3)
    assert result.min() >= 0
    assert result.max() <= 1
```

## 📚 Documentation

### When to Update Documentation
Update docs when you:
- Add new features
- Change existing functionality
- Fix bugs that affect usage
- Modify installation process
- Add dependencies

### Documentation Files to Update
- **README.md**: Main project overview
- **QUICKSTART.md**: Quick start guide
- **CODE_STRUCTURE.md**: Architecture details
- **DATASET_INFO.md**: Dataset information
- **Inline comments**: Code documentation

## 🔀 Pull Request Process

### Before Submitting
1. **Update documentation** as needed
2. **Test thoroughly** on your local machine
3. **Review your changes** using `git diff`
4. **Ensure clean commit history**
5. **Rebase on latest main** if needed

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tested locally
- [ ] All existing features work
- [ ] No new errors in console

## Screenshots (if applicable)
Add screenshots showing changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings/errors
- [ ] Commits are clean and descriptive
```

### Review Process
1. **Automated checks**: Ensure CI passes (if configured)
2. **Code review**: Maintainer reviews code
3. **Feedback**: Address reviewer comments
4. **Approval**: PR is approved
5. **Merge**: Maintainer merges PR

### After Merge
1. **Delete branch**: Clean up your branch
2. **Update local**: Pull latest changes
3. **Close issues**: Link and close related issues

## 🎯 Priority Areas for Contribution

### High Priority
1. **Unit tests**: Add test coverage
2. **Error handling**: Improve robustness
3. **Documentation**: Expand guides and tutorials
4. **Performance**: Optimize model inference
5. **Security**: File upload validation

### Medium Priority
1. **Batch processing**: Process multiple images
2. **Result history**: Store predictions
3. **Advanced UI**: Improve user interface
4. **API documentation**: Add API specs
5. **Mobile support**: Responsive design

### Low Priority (Nice to Have)
1. **Docker support**: Containerization
2. **Cloud deployment**: AWS/GCP guides
3. **Visualization**: Show affected areas on map
4. **Multi-language**: i18n support
5. **Analytics**: Usage statistics

## 💬 Communication

### Where to Ask Questions
- **GitHub Issues**: For bugs and features
- **Pull Request comments**: For code discussion
- **README**: For general information

### Response Times
- Issues: We aim to respond within 1-3 days
- PRs: Initial review within 3-7 days
- Please be patient - this is a volunteer project!

## 🏆 Recognition

Contributors will be:
- Acknowledged in release notes
- Listed in contributors section
- Given credit in documentation
- Appreciated for their efforts! 🎉

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## 🙏 Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort!

---

**Questions?** Feel free to open an issue or reach out to the maintainers.

**Ready to contribute?** Check out the [open issues](https://github.com/samarthpatilML/Flood-Detection-Using-Deep-Learning-Model-From-Satellite-Images-/issues) and get started!
