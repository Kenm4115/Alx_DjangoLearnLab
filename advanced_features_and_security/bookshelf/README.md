# Permissions and Groups Setup

## Overview
This application uses Django's built-in groups and permissions to restrict access. Custom permissions have been added to the `Post` model, and groups (Viewers, Editors, Admins) have been configured with varying levels of access.

## Usage
- Add users to groups via the admin panel or using management scripts.
- Ensure views are protected with appropriate permission checks.

## Testing
- Log in with users assigned to different groups and verify access levels.
