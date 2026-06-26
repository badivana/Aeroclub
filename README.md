# ✈️ Aero Club Nitte — Official Website

The official website for **Aero Club NMAMIT Nitte** — a student-run aviation and aerospace club. Built with Node.js, Express, and EJS, it showcases events, team members, projects, gallery, achievements, and provides a contact/mail form.

---

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v18 or higher
- npm (comes with Node.js)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/badivana/aeroclub-main.git
cd aeroclub-main

# 2. Install dependencies
npm install

# 3. Start the development server (with hot reload)
npm run dev
```

The server will start at **http://localhost:5000**

---

## 📁 Project Structure

```
aeroclub-main/
├── index.js               # Main Express server entry point
├── sendmail.js            # Nodemailer email handler
├── package.json           # Project metadata & dependencies
│
├── views/                 # EJS templates (server-rendered pages)
│   ├── index.ejs          # Home page
│   ├── events.ejs         # Events listing
│   ├── projects.ejs       # Projects showcase
│   ├── team.ejs           # Team members
│   ├── mentors.ejs        # Mentors
│   ├── gallery.ejs        # Photo gallery
│   ├── achievement.ejs    # Achievements
│   ├── contact.ejs        # Contact form
│   ├── register.ejs       # Event registration
│   └── privacy-policy.ejs # Privacy policy
│
├── events_vayu/           # Static HTML pages for individual events
│   ├── aeroX.html
│   ├── rotorCraft.html
│   ├── skyProbe.html
│   ├── vichaar.html
│   └── wordsWithWings.html
│
├── assets/                # Static assets served publicly
│   ├── css/               # Stylesheets
│   ├── js/                # Client-side JavaScript
│   ├── img/               # Images
│   └── vendor/            # Third-party libraries
│
└── forms/                 # Legacy form files
```

---

## 🌐 Available Routes

| Route | Description |
|---|---|
| `GET /` | Home page |
| `GET /home` | Home page (alias) |
| `GET /events` | Events page |
| `GET /projects` | Projects page |
| `GET /team` | Team members |
| `GET /mentors` | Mentors |
| `GET /gallery` | Photo gallery |
| `GET /achievement` | Achievements |
| `GET /contact` | Contact page |
| `GET /register` | Event registration |
| `GET /privacy-policy` | Privacy policy |
| `GET /aerox` | AeroX event page |
| `GET /rotorcraft` | RotorCraft event page |
| `GET /skyprobe` | SkyProbe event page |
| `GET /vichaar` | Vichaar event page |
| `GET /words_with_wings` | Words With Wings event page |
| `GET /aeroX` | AeroX detail (events_vayu) |
| `GET /rotorCraft` | RotorCraft detail (events_vayu) |
| `GET /skyProbe` | SkyProbe detail (events_vayu) |
| `GET /wordsWithWings` | Words With Wings detail (events_vayu) |
| `POST /mail` | Send contact form email |

---

## 📬 Contact Form / Email

The `/mail` endpoint accepts a `POST` request with the following body:

```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "subject": "Subject line",
  "message": "Your message"
}
```

Emails are sent via **Nodemailer** using Gmail SMTP to `aeroclubnitte@nmamit.in`.

> ⚠️ **Important:** The Gmail App Password in `sendmail.js` is hardcoded. Move it to a `.env` file before deploying to production (see below).

---

## 🔐 Environment Variables (Recommended for Production)

Create a `.env` file in the root directory:

```env
PORT=5000
MAIL_USER=queriesaeroclubnitte@gmail.com
MAIL_PASS=your_gmail_app_password
```

Then update `sendmail.js` to use:

```js
const dotenv = require('dotenv');
dotenv.config();

auth: {
  user: process.env.MAIL_USER,
  pass: process.env.MAIL_PASS
}
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Node.js |
| Framework | Express.js v4 |
| Template Engine | EJS |
| Email | Nodemailer (Gmail SMTP) |
| Dev Server | Nodemon |
| Deployment | Vercel (configured) |

---

## 📜 npm Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start server with Nodemon (hot reload) |
| `npm start` | Start server via npx nodemon |

---

## ☁️ Deployment

This project is pre-configured for **Vercel** deployment (`.vercel` in `.gitignore`). To deploy:

```bash
npm install -g vercel
vercel
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

ISC License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  Made with ❤️ by <strong>Aero Club NMAMIT Nitte</strong>
</div>
