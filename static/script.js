document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const copyBtn = document.getElementById('copy-btn');
    const generateBtn = document.getElementById('generate-btn');
    const lengthSlider = document.getElementById('length');
    const lengthValue = document.getElementById('length-value');
    const lowercaseCheckbox = document.getElementById('lowercase');
    const uppercaseCheckbox = document.getElementById('uppercase');
    const numbersCheckbox = document.getElementById('numbers');
    const symbolsCheckbox = document.getElementById('symbols');

    // Update length display when slider changes
    lengthSlider.addEventListener('input', () => {
        lengthValue.textContent = lengthSlider.value;
    });

    // Ensure at least one checkbox is always selected
    const checkboxes = [lowercaseCheckbox, uppercaseCheckbox, numbersCheckbox, symbolsCheckbox];
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCount = checkboxes.filter(cb => cb.checked).length;
            if (checkedCount === 0) {
                checkbox.checked = true;
            }
        });
    });

    // Generate password
    async function generatePassword() {
        const options = {
            length: parseInt(lengthSlider.value),
            lowercase: lowercaseCheckbox.checked,
            uppercase: uppercaseCheckbox.checked,
            numbers: numbersCheckbox.checked,
            symbols: symbolsCheckbox.checked
        };

        try {
            generateBtn.textContent = 'Generating...';
            generateBtn.disabled = true;

            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(options)
            });

            if (!response.ok) {
                throw new Error('Failed to generate password');
            }

            const data = await response.json();
            passwordInput.value = data.password;
        } catch (error) {
            console.error('Error:', error);
            passwordInput.value = 'Error generating password';
        } finally {
            generateBtn.textContent = 'Generate Password';
            generateBtn.disabled = false;
        }
    }

    // Copy to clipboard
    async function copyToClipboard() {
        if (!passwordInput.value || passwordInput.value === 'Error generating password') {
            return;
        }

        try {
            await navigator.clipboard.writeText(passwordInput.value);
            copyBtn.classList.add('copied');
            setTimeout(() => {
                copyBtn.classList.remove('copied');
            }, 1500);
        } catch (error) {
            // Fallback for older browsers
            passwordInput.select();
            document.execCommand('copy');
            copyBtn.classList.add('copied');
            setTimeout(() => {
                copyBtn.classList.remove('copied');
            }, 1500);
        }
    }

    // Event listeners
    generateBtn.addEventListener('click', generatePassword);
    copyBtn.addEventListener('click', copyToClipboard);

    // Generate password on page load
    generatePassword();
});
