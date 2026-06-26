require("dotenv").config();
const nodemailer = require("nodemailer");

module.exports.sendmail = async (name, email, subject, explain) => {
  const transporter = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 587,
    secure: false,
    auth: {
      user: process.env.MAIL_USER,
      pass: process.env.MAIL_PASS,
    },
    tls: { rejectUnauthorized: false },
  });

  const mailoptions = {
    from: process.env.MAIL_USER,
    to: "aeroclubnitte@nmamit.in",
    subject: `${subject}`,
    text: `Name: ${name}\nEmail: ${email}\nSubject: ${subject}\nBody: ${explain}`,
  };

  transporter.sendMail(mailoptions, (err, res) => {
    if (err) {
      console.log("Error sending mail:", err);
    } else {
      console.log("Mail successfully sent:", res.messageId);
    }
  });
};
