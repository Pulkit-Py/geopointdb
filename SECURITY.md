# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security issues seriously. If you discover a security vulnerability in GeoPointDB, we appreciate your help in disclosing it to us in a responsible manner.

### How to Report a Security Issue

Please report security issues by emailing the maintainer at pulkitsaini127@gmail.com with the subject line: "[GeoPointDB] Security Vulnerability".

In your report, please include:
- A description of the vulnerability
- Steps to reproduce the issue
- Any relevant code or configuration
- The version of GeoPointDB you're using
- Any potential impact of the vulnerability

We will acknowledge your email within 48 hours and will do our best to send a more detailed response within 72 hours indicating the next steps in handling your report.

### Security Updates

Security updates will be released as patch versions. We recommend always using the latest stable version of GeoPointDB.

### Security Considerations

- GeoPointDB is designed to work with local SQLite databases and does not require internet access by default.
- The package only includes read operations by default, which limits potential attack vectors.
- Always validate and sanitize any input before passing it to GeoPointDB methods.

### Security Best Practices

1. Keep your Python environment and dependencies up to date.
2. Only use the package with trusted data sources.
3. Regularly check for updates to GeoPointDB to receive security patches.
4. Review the code if you're using a forked or modified version of the package.

### Public Disclosure

We follow responsible disclosure practices. Security issues will be disclosed publicly after a fix is available, typically in the form of a new release.
