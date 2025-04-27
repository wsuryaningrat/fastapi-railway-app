# API Documentation

This project provides an API for text emotion prediction using the `w11wo/indonesian-roberta-base-predict-id` model deployed on Railway. Below are the details of the two endpoints available:

---

## Base URL
`https://<your-deployed-url>.up.railway.app`

Replace `<your-deployed-url>` with the actual domain of your deployed application.

---

## 1. `GET /`

### Description:
Returns a welcome message indicating the server is running.

### Example Request:
```bash
GET https://<your-deployed-url>.up.railway.app/
