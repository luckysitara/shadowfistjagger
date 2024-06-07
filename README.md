# shadowfistjagger
A Platform to connects Web3 founder with Security Professionals to audit and  test the security  of their softwares
Sure, here's an example documentation for the API endpoints along with guidelines for developers to interact with the backend:

---

## Backend  Documentation

### Base URL:
```
http://github.com/luuckysitara/shadowfistjagger.git/README.md
```

### Authentication:
- **Register User**
  - **URL:** `/auth/register`
  - **Method:** POST
  - **Request Body:** `{ "username": "your_username", "password": "your_password" }`
  - **Response:** `{ "msg": "User created successfully" }`

- **Login User**
  - **URL:** `/auth/login`
  - **Method:** POST
  - **Request Body:** `{ "username": "your_username", "password": "your_password" }`
  - **Response:** `{ "access_token": "your_access_token" }`

### Projects:
- **Submit Project**
  - **URL:** `/projects/submit`
  - **Method:** POST
  - **Authorization Header:** `Bearer your_access_token`
  - **Request Body:** `{ "project_id": "your_project_id", "details": "project_details" }`
  - **Response:** `{ "msg": "Project submitted successfully" }`

### Bugs:
- **Report Bug**
  - **URL:** `/bugs/report`
  - **Method:** POST
  - **Authorization Header:** `Bearer your_access_token`
  - **Request Body:** `{ "project_id": "project_id", "description": "bug_description" }`
  - **Response:** `{ "msg": "Bug reported successfully" }`

### Bounties:
- **Create Bounty**
  - **URL:** `/bounties/create`
  - **Method:** POST
  - **Authorization Header:** `Bearer your_access_token`
  - **Request Body:** `{ "project_id": "project_id", "amount": "bounty_amount" }`
  - **Response:** `{ "msg": "Bounty created successfully" }`

- **Claim Bounty**
  - **URL:** `/bounties/claim`
  - **Method:** POST
  - **Authorization Header:** `Bearer your_access_token`
  - **Request Body:** `{ "bounty_id": "bounty_id" }`
  - **Response:** `{ "msg": "Bounty claimed successfully" }`

---

### Guidelines for Developers:
1. **Registration and Authentication:**
   - Register a new user using the `/auth/register` endpoint.
   - Login using the `/auth/login` endpoint to obtain an access token.

2. **Projects:**
   - Submit a new project using the `/projects/submit` endpoint.
   - Provide the project details including project ID and description.

3. **Bugs:**
   - Report a bug related to a project using the `/bugs/report` endpoint.
   - Include the project ID and bug description in the request body.

4. **Bounties:**
   - Create a new bounty for a project using the `/bounties/create` endpoint.
   - Specify the project ID and bounty amount.
   - Claim a bounty using the `/bounties/claim` endpoint by providing the bounty ID.

5. **Authorization:**
   - Include the access token in the Authorization header (`Bearer your_access_token`) for protected endpoints.

6. **Response Format:**
   - All endpoints return JSON responses with appropriate status codes.
   - Handle responses accordingly in your application.


