import confetti from 'https://cdn.skypack.dev/canvas-confetti';

// Trigger the confetti animation when the script runs
confetti();

// Redirect to the homepage after 15 seconds
setTimeout(() => {
    window.location.href = "/";
}, 15000); // 15 seconds