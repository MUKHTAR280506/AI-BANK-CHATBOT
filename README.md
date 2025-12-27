# 🏦 AI BANK CHATBOT

End-to-end AI-powered banking chatbot with admin controls, compliance checks, and LLM-driven intelligence.

---

## 🔹 PROJECT HIGHLIGHTS
- Conversational AI banking assistant
- Secure fund transfer simulation
- Sanctions & rule validation using RAG
- Admin dashboard for full control
- Real-world BFSI-style architecture
- Built for AI Engineer / ML Engineer / Data Scientist roles

---

## 🔹 TECH STACK

### Frontend
- React (Vite)
- JavaScript
- Custom CSS
- Fetch API

### Backend
- FastAPI
- Python
- SQLAlchemy
- LangChain
- OpenAI API
- Vector DB (Qdrant)
- SQLite / PostgreSQL

---

## 🔹 SYSTEM ARCHITECTURE
React UI
↓
FastAPI Backend
↓
SQL DB (Accounts, Transactions, Beneficiaries)
↓
Vector DB (Rules, Sanctions)
↓
OpenAI LLM (via LangChain)



---

## 🔹 CUSTOMER FEATURES
- AI chatbot interface
- Add beneficiary
- Transfer funds
- Balance check
- Transaction history (last 10)
- Automatic complaint detection
- Sentiment & severity analysis

---

## 🔹 ADMIN FEATURES
- Upload sanctions / rules documents
- Configure daily & per-transaction limits
- View all customers & balances
- Credit / Debit customer wallets
- View & delete beneficiaries
- Compliance rule management

---

## 🔹 AI & ML FEATURES
- Intent detection
- Sentiment analysis
- Complaint classification
- Retrieval-Augmented Generation (RAG)
- Embedding-based similarity search
- LLM-based compliance decisioning
- Agent-based architecture

---

## 🔹 CORE FLOWS

### Fund Transfer
- User → Chat UI
- Backend validation:
  - Numeric amount
  - Balance check
  - Per-transaction limit
  - Daily limit
  - Sanctions (RAG)
- LLM approval / rejection
- Transaction execution
- Balance update

### Complaint Detection
- User message analysis
- Sentiment scoring
- Severity classification
- Complaint category detection
- CRM record creation
- User notification

---

## 🔹 DATABASE TABLES
- accounts (user_id, balance)
- beneficiaries (user_id, name, iban, bank, country)
- transactions (amount, type, status)
- transfer_limits (daily_limit, per_transaction_limit)
- crm_complaints (complaint, category, severity)

---

## 🔹 AUTHENTICATION (DEMO)
- Basic Authentication
- Role-based access
  - Admin
  - Customer
- Backend-side validation
- Row-level locking for transactions

---

## 🔹 PROJECT STRUCTURE

AI-BANK-CHATBOT/
├── backend/
│ ├── app/
│ │ ├── routes/
│ │ ├── agents/
│ │ ├── rag/
│ │ ├── models/
│ │ ├── schemas/
│ │ └── core/
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── auth/
│ │ └── styles/
│ └── package.json
│
├── README.md
└── .gitignore


---

## 🔹 HOW TO RUN

clone the repository to your computer using git commands. 

### Backend
run docker-compose up --build to get the docker images


cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

Run backend server 
uvicorn app.main:app --reload

To run front end
cd frontend
npm install
npm run dev

initialize db creations
python -m app.core.init_db

Add a user customer  and balance in accounts table



🔹 SAMPLE CREDENTIALS
Role	Username	Password
Admin	 admin	    admin
Customer customer	customer

FUTURE ENHANCEMENTS

Fraud detection ML model

Kafka real-time streaming

SHAP explainability

JWT / OAuth2 authentication

Docker & Kubernetes deployment

CI/CD pipelines

AUTHOR

Mukhtar Ahmad
AI Chatbot Developer | NLP Engineer | Data Scientist

GitHub: https://github.com/MUKHTAR280506

LinkedIn: https://www.linkedin.com/in/mukhtar280506/

🔒 Repository is private. Access available on request.

images-![Admin customer management](https://github.com/user-attachments/assets/805733cc-f8a7-49e4-a7b9-c8b6eaff42f5)
![chatbot beneficiary addition](https://github.com/user-attachments/assets/4ada4524-cac5-4f1f-9a23-45154db9a4ff)
![chatbot complaint registration](https://github.com/user-attachments/assets/47626507-7a36-49e1-a7f0-2a6e62230975)
![chatbot funds transfer](https://github.com/user-attachments/assets/56746935-9d72-4931-8ccd-798b4ab6665c)
![chatbot transaction history](https://github.com/user-attachments/assets/eb976c73-aaa0-4cd9-9aa7-8ce7e2cb7414)
![login_page](https://github.com/user-attachments/assets/446b64eb-db1d-48b5-a6cd-8ddfd8af2fda)
![admin page 1](https://github.com/user-attachments/assets/4d1561ac-640d-485c-ae36-d4338863ee64)




