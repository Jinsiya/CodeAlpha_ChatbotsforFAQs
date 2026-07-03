document.addEventListener('DOMContentLoaded', function() {
    const messages = document.getElementById('messages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatContainer = document.getElementById('chatContainer');
    const typingIndicator = document.getElementById('typingIndicator');
    const themeToggle = document.getElementById('themeToggle');

    // Send message function
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Disable input
        userInput.disabled = true;
        sendBtn.disabled = true;

        // Add user message
        addMessage(message, 'user');
        userInput.value = '';

        // Show typing indicator
        showTyping();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            // Hide typing indicator
            hideTyping();

            // Add bot response
            if (data.answer) {
                addMessage(data.answer, 'bot', data.confidence);
            } else {
                addMessage("Sorry, I couldn't process your request.", 'bot');
            }

        } catch (error) {
            console.error('Error:', error);
            hideTyping();
            addMessage("Sorry, I'm having trouble connecting. Please try again.", 'bot');
        }

        // Re-enable input
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
        scrollToBottom();
    }

    // Add message to chat
    function addMessage(text, sender, confidence = null) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.innerHTML = sender === 'user' ? 
            '<i class="fas fa-user"></i>' : 
            '<i class="fas fa-robot"></i>';
        
        const textDiv = document.createElement('div');
        textDiv.className = 'message-text';
        
        const p = document.createElement('p');
        p.textContent = text;
        textDiv.appendChild(p);
        
        // Add confidence score if available
        if (confidence && confidence > 0.1) {
            const confidenceSpan = document.createElement('span');
            confidenceSpan.style.cssText = `
                font-size: 11px;
                color: #94a3b8;
                display: block;
                margin-top: 6px;
            `;
            const percentage = Math.round(confidence * 100);
            confidenceSpan.textContent = `Confidence: ${percentage}%`;
            textDiv.appendChild(confidenceSpan);
        }
        
        contentDiv.appendChild(avatar);
        contentDiv.appendChild(textDiv);
        messageDiv.appendChild(contentDiv);
        
        messages.appendChild(messageDiv);
        scrollToBottom();
    }

    // Show typing indicator
    function showTyping() {
        typingIndicator.classList.remove('hidden');
        scrollToBottom();
    }

    // Hide typing indicator
    function hideTyping() {
        typingIndicator.classList.add('hidden');
    }

    // Scroll to bottom
    function scrollToBottom() {
        setTimeout(() => {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }, 100);
    }

    // Toggle theme
    function toggleTheme() {
        document.body.classList.toggle('dark-mode');
        const icon = themeToggle.querySelector('i');
        if (document.body.classList.contains('dark-mode')) {
            icon.className = 'fas fa-sun';
            localStorage.setItem('theme', 'dark');
        } else {
            icon.className = 'fas fa-moon';
            localStorage.setItem('theme', 'light');
        }
    }

    // Check saved theme
    function checkDarkMode() {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark') {
            document.body.classList.add('dark-mode');
            themeToggle.querySelector('i').className = 'fas fa-sun';
        }
    }

    // Event Listeners
    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Suggestion chips
    document.querySelectorAll('.chip').forEach(chip => {
        chip.addEventListener('click', function() {
            const question = this.dataset.question;
            if (question) {
                userInput.value = question;
                sendMessage();
            }
        });
    });

    themeToggle.addEventListener('click', toggleTheme);

    // Check dark mode on load
    checkDarkMode();
    
    // Focus input on load
    userInput.focus();
});