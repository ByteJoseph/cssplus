document.addEventListener('readystatechange', function() {
            if (document.readyState === 'loading') {
                document.body.style.display = 'none';
            }
        });

document.addEventListener('DOMContentLoaded', () => {
    async function sendStylesToServer() {
        if (!navigator.onLine) {
            console.log('No internet connection.');
            return;
        }
        const scriptTags = document.querySelectorAll('script[src*="cssplus.onrender.com"]');
        const targetURL = scriptTags.length > 0 ? 'https://cssplus.onrender.com/compile/' : 'http://127.0.0.1:8000/compile/';
        const styleElements = document.querySelectorAll('style');
        for (const style of styleElements) {
            const cssContent = style.textContent;
            const encodedCSSContent = encodeURIComponent(cssContent);
            try {
                const response = await fetch(`${targetURL}?var=${encodedCSSContent}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                let compiledCSS = await response.text();
               /* console.log('Compiled CSS received:');
                console.log(compiledCSS);  */
                compiledCSS = compiledCSS.replace(/^"|"$/g, '').replace(/{{}/g, '');
                const styleElement = document.createElement('style');
                styleElement.textContent = compiledCSS;
                document.head.appendChild(styleElement);
            } catch (error) {
                console.error('Error sending style content:', error);
            }
        }
    }
    sendStylesToServer();
    document.body.style.display = 'block';
});
