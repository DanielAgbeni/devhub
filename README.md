# DevHub: Intelligent Matchmaking Platform for Developers 💻🤝

<a href="https://discord.gg/u86Gy2qFHm" target="_blank"><img src="https://img.shields.io/discord/1259889923129999411?style=flat&colorA=000000&colorB=000000&label=discord&logo=discord&logoColor=ffffff" /></a>


DevHub is an innovative platform designed to connect developers who share similar interests and complementary skills. By leveraging advanced technologies, it facilitates intelligent matchmaking and personalized recommendations, enabling devs to form effective teams and engage in meaningful collaborations. The platform provides a structured and user-friendly environment for networking, learning, and growth, ultimately enhancing the academic and professional experiences of developers.

## Tech Stacks 🛠️

- **Backend**: Flask 🐍 + LangChain 🔗  
- **Frontend**: Vite + React (TypeScript) ⚛️  
- **Database**: Neo4j + MongoDB 

## Features ✨

- [x] **OTP Based Authentication** (Email Verification)
- [x] **Signin/Signup** (Unique Username check and follows NIST Guidlines Validation) 
- [x] **Sharable Profiles** (Share your profile with others)
- [x] **Add/Remove Friends** (Follow others to make friends)
- [x] **Add/update/delete projects** (Supports Banner image,Markdown in Desc and tech-stack tag selection)
- [x] **Add Github and Leetcode profiles** (Data in profile will be populated from the given coding accounts)
- [x] **Convert Profile into Knowledge Graphs** 
- [x] **Recomendation Engine** (Graph Traversal techniques)
- [x] **Use langchain to Chat with KGs**
- [x] **Saved Chat history**
- [x] **Typing animation and Markdown response**  
- [x] **Share projects with unique projectID**
- [x] **Star your and other user's project**
- [x] **Visualize your Relation in Graph using d3**
- [x] **Add Neo4j account, get graph Schema and Execute your query**
- [x] **Save image as png of graph and also share it with others using shareable link**
- [x] **Feed Section** (Common section where Users can post images with description and tags)
- [x] **Users can see and share particular post**
- [x] **Upvote and Downvote Posts**
- [x] **comment on posts**
- [x] **Developer Directory to find registered developers**
- [x] **Chat with other developers** (Find and message others)
- [X] **Settings** (Update profile details and webapp theme and much more)
- [x] **Help, Docs, Feedback and Contact for support**
- [x] **Responsive Design**
- [x] **Supports Dark Mode**
 
## Local Installation 🧑🏻‍💻

Enter into the root directory.
```bash
cd devhub
```
You can use `setup.bat` to automate the installation and running process of the webapp. (make sure to make `.env` in server and populate it with the data)

```bash
./setup.bat
```
### Manual Installation ⚒️

1. Open two terminal for server and client and enter into the directories.

    ```bash
    ## 1st terminal for server
    cd server

    ## create .env file with following details (you can create your neo4j account or use our mirror database credentials)

    GOOGLE_API_KEY= 
    SECRET_KEY=
    NEO4J_URI= 
    NEO4J_USER=
    NEO4J_PASSWORD=
    MONGODB_URI=
    CLOUDINARY_NAME=
    CLOUDINARY_API_KEY=
    CLOUDINARY_API_SECRET=

    ## Join our discord server to get Mirror Database Credentials.
    Discord Server Link : https://discord.gg/u86Gy2qFHm
    ```
    ```bash
    ## Create and activate Virtual Environment
    python -m venv venv

    ./venv/Scripts/activate
    ```

    ```bash
    ## Install dependencies
    pip install -r requirements.txt
    ```
    ```bash
    ## Run the Server
    flask run or python server.py
    ```

    ```bash
    ## 2nd terminal for client
    cd client

    ## Install dependencies
    npm install

    ## Run the client
    npm run dev
    ```

### Docker Installation 🐋

1. Pull the devhub-server image from the dockerhub

    ```bash
    docker pull deepraj21/devhub-server:latest
    ```
2. Go into the server directory having .env file to run the image into a container

    ```bash
    docker run -d -p 5000:5000 --name devhub-server --env-file .env deepraj21/devhub-server:latest
    ```

## API Documentation 📜

Our API is designed to give you access to all core functionalities of DevHub programmatically. You can interact with the platform's matchmaking, user profile creation, and project exploration features via HTTP requests. To get started with the API, please refer to our Postman documentation, which provides detailed information on all available endpoints.

<a href="https://documenter.getpostman.com/view/37803453/2sAXxP9Cxo" target="_blank"><img src="https://img.shields.io/badge/Postman-View%20Documentation-orange?style=flat&logo=postman" /></a>

## Conclusion 🎉
By integrating LLMs for natural language understanding, LangChain for workflow enhancement, and Neo4j for advanced data storage and querying, DevHub offers a comprehensive solution for devs seeking meaningful collaborations. This combination not only enhances user experience but also ensures that connections are based on relevant skills and interests, leading to more effective teamwork.

## Contribution

See the [CONTRIBUTION GUIDE](https://github.com/devhub-ai/devhub/blob/main/.github/CONTRIBUTING.md) to get started.
