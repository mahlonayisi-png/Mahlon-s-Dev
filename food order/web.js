// Order Now Function with Toast Notification
function orderNow(dishName) {
  const toast = document.getElementById('toast');
  toast.textContent = `🛒 "${dishName}" has been added to your order!`;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

// Animate cards on scroll using Intersection Observer
const cards = document.querySelectorAll('.dish-card');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }, index * 100);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

// Set initial state for animation
cards.forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(30px)';
  card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(card);
});
