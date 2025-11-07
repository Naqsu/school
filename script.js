document.addEventListener('DOMContentLoaded', () => {

    function isPrime(n) {
        if (n < 2) return false;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) {
                return false;
            }
        }
        return true;
    }

    const generators = document.querySelectorAll('.prime-generator');

    generators.forEach(generator => {
        const button = generator.querySelector('.prime-button');
        const display = generator.querySelector('.prime-display');

        let currentPrime = 2;
        let nextPrimeCandidate = 2;

        function render() {
            display.textContent = currentPrime;
        }

        button.addEventListener('click', () => {
            nextPrimeCandidate++;

            while (!isPrime(nextPrimeCandidate)) {
                nextPrimeCandidate++;
            }

            currentPrime = nextPrimeCandidate;

            render();
        });
        render();
    });

});