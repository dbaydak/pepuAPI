# Admitad Statistics API

This Python project provides a wrapper for the Admitad API, enabling easy access to statistics and deeplink generation functionality.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Examples](#examples)
- [Configuration](#configuration)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [Further Development](#further-development)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetch actions statistics from Admitad API
- Generate deeplinks for campaigns
- Customizable date ranges for reports
- Authentication handling with client credentials
- Support for SubID tracking parameters
- Response pagination handling

## Prerequisites

* Python 3.7 or higher
* Admitad account with API credentials
* Active campaign access

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd admitad-statistics-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file:
   In the `variables` directory, create a file named `.dev.env` with your Admitad API credentials:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

2. Verify installation:
```bash
python publisher_reports.py
```

## Usage

### Fetch Statistics
```bash
python publisher_reports.py
```

This will fetch and print actions data from the last 5 days.

### Generate Deeplinks
```bash
python deeplink_generator.py
```

## Code Overview

* **`authorization.py`:** Handles authentication with the Admitad API.
    * `get_base64_authorization()`: Encodes client ID and secret for basic authentication.
    * `get_token()`: Retrieves an access token using client credentials grant type.
    * `get_access_token()`: Extracts the access token from the token response.
* **`publisher_reports.py`:** Fetches statistics data.
    * `get_admitad_statistics_by_actions()`: Retrieves actions data with specified parameters.
* **`deeplink_generator.py`:** Handles deeplink generation.
    * `admitad_deeplink()`: Generates tracking links for specific campaigns and URLs.

## Examples

### Fetch Statistics
```python
from publisher_reports import get_admitad_statistics_by_actions

stats = get_admitad_statistics_by_actions()
print(stats)
```

### Generate Deeplink
```python
from deeplink_generator import admitad_deeplink

deeplink = admitad_deeplink(
    campaign_id=39121,
    upl='https://example.com',
    subid='tracking_id'
)
print(deeplink)
```

## Configuration

The application uses environment variables for configuration. Required variables in `.dev.env`:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

Never commit your `.dev.env` file to version control.

## Customization

### Statistics Parameters
* **Date range:** Modify `date_start` and `date_end` parameters
* **Limit and offset:** Adjust `limit` and `offset` for pagination
* **Ordering:** Change `order_by` parameter for different sorting

### Deeplink Parameters
* Campaign ID
* Landing page URL
* SubID tracking parameters (subid, subid1, subid2, etc.)

## Error Handling

The API wrapper includes basic error handling for:
- Authentication failures
- Invalid API responses
- Network errors

Example error handling:
```python
try:
    stats = get_admitad_statistics_by_actions()
except Exception as e:
    print(f"Error fetching statistics: {e}")
```

## Further Development

Planned improvements:
* Enhanced error handling and logging
* Additional statistics endpoints support
* Command-line interface
* Async API support
* Comprehensive test suite
* Rate limiting implementation
* Response caching

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Requirements

All required packages are listed in `requirements.txt`:
- requests~=2.32.3
- python-dotenv~=1.0.1