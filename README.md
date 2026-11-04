# chronicle-api
Chronicle API turns long, complex text such API description into short, clear, and actionable summaries

# Chronicle-API, Smart Note Summarizer API


#### Description:
The Smart Note Summarizer API is a lightweight, asynchronous RESTful service built with FastAPI and Python. It manages personal notes and uses Google's Gemini API (`google-genai` SDK) to generate concise, automated AI summaries of stored notes.

---

## Project Overview & Problem Statement

In modern software development and daily engineering workflows, developers frequently face extreme information overload. Skimming through lengthy documentation, dense meeting logs, or extensive database records to find core takeaways is inefficient and time-consuming. When engineers lack immediate clarity on what is inside a piece of content, productivity stalls.

This project is a lightweight, asynchronous RESTful microservice built using [FastAPI](https://fastapi.tiangolo.com/). It acts as an intelligent backend processing layer that leverages the [Google Gemini API](https://ai.google.dev/) to digest, reiterate, and condense dense text into clear, actionable insights.

Beyond text transformation, this service resolves critical **security and architectural challenges**:

1. **Information Abstraction**: Engineers often need to understand the core context of a document without exposing raw, sensitive full-length text across client-side applications. This service acts as a security buffer, returning structured summaries that give engineers *just enough* context to act without exposing the full raw payload to untrusted environments.
2. **Secrets Isolation**: Client applications (browsers or mobile apps) should never interact directly with third-party AI providers. This microservice encapsulates API credentials securely on the server side, ensuring zero credential leakage.

---

## Project Structure

```text
├── main.py              # Main FastAPI application and route handlers
├── requirements.txt     # Dependencies
├── .env.example         # Template for environment variables
├── README.md            # Project documentation
└── notes_db.json        # (Optional) Local storage/mock DB for notes

---

## System Architecture

The application implements a classic **3-Tier Architecture**:

```text
[ Frontend / Client ] <---> [ FastAPI Microservice ] <---> [ Gemini API / Database ]
  (User Interface)            (Security & Logic Layer)        (Raw Data & Intelligence)

---

## Additional Notes

Always check Gemini API documentation for latest update and to change the model depending on your model requirements.


