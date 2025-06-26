function submitForm() {
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const problem = document.getElementById("problem").value;

  if (!email || !phone || !problem) {
    alert("Please fill in all fields before submitting.");
    return;
  }

  alert("Form submitted!\n\nEmail: " + email + "\nPhone: " + phone + "\nProblem: " + problem);
  document.getElementById("popupForm").style.display = "none";
}

function closeForm() {
  document.getElementById("popupForm").style.display = "none";
}

document.addEventListener('dialogflow-response', function(event) {
  const response = event.detail;

  if (response.richContent) {
    response.richContent.forEach(group => {
      group.forEach(item => {
        if (item.type === 'custom' && item.text && item.text.startsWith('<style>')) {
          const styleTag = document.createElement('style');
          styleTag.innerHTML = item.text.replace('<style>', '').replace('</style>', '');
          document.head.appendChild(styleTag);
        }
      });
    });
  }

  if (response.fulfillmentMessages) {
    response.fulfillmentMessages.forEach(msg => {
      if (msg.payload?.custom_event === "bot_message" && msg.payload.text) {
        const para = document.querySelector('.test-para');
        para.textContent += msg.payload.text + "\n";
        para.scrollTop = para.scrollHeight;
      }
    });
  }
});
