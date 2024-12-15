



POST /api/posts/
Headers:
  Authorization: Token <your_token>
Body:
{
    "title": "My First Post",
    "content": "This is the content of the post."
}


Endpoints for follow/unfollow.
Example requests and responses.
Feed functionality details.

## Follow a User
- **URL:** `/api/accounts/follow/<user_id>/`
- **Method:** POST
- **Authorization:** Token required

### Request:


### Response:
```json
{
    "message": "You are now following john_doe."
}

URL: /api/posts/feed/
Method: GET
Authorization: Token required
[
    {
        "id": 1,
        "author": "john_doe",
        "title": "First Post",
        "content": "This is the first post.",
        "created_at": "2024-12-15T10:00:00Z"
    }
]

## Like a Post
- **URL:** `/api/posts/<post_id>/like/`
- **Method:** POST
- **Authorization:** Token required
- **Response:**
  ```json
  {
      "message": "Post liked."
  }

URL: /api/notifications/
Method: GET
Authorization: Token required
Response:
[
    {
        "id": 1,
        "actor": "user1",
        "verb": "liked your post",
        "timestamp": "2024-12-15T10:00:00Z",
        "is_read": false
    }
]

