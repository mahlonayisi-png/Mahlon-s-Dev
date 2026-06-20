let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

function updateSlider() {
  const container = document.querySelector('.slider-container');
  container.scrollLeft = currentSlide * 300;

  dots.forEach(dot => dot.classList.remove('active'));
  dots[currentSlide].classList.add('active');
}

function moveSlide(direction) {
  currentSlide = (currentSlide + direction + slides.length) % slides.length;
  updateSlider();
}

function goToSlide(index) {
  currentSlide = index;
  updateSlider();
}

// Auto-slide every 4 seconds
setInterval(() => moveSlide(1), 4000);



    // 1. Initialize the cart count
    let cartCount = 0;

    // 2. Target the Cart text element
    // Since your text currently reads "🛒 Cart ( 0 )", we will find it using its content
    const elements = document.querySelectorAll('div, p, a, li');
    let cartElement = null;

    elements.forEach(el => {
        if (el.textContent.includes('🛒 Cart')) {
            cartElement = el;
        }
    });

    // 3. Find all the "Order Now" / "order now" buttons on your page
    const orderButtons = document.querySelectorAll('button, input[type="button"], .order-btn');

    // 4. Attach the click event to each button
    orderButtons.forEach(button => {
        // Only target actual ordering buttons, ignoring header or main banner buttons if necessary
        if (button.textContent.toLowerCase().includes('order now')) {
            button.addEventListener('click', (e) => {
                e.preventDefault(); // Prevents page from jumping if it's a link
                
                // Increase counter
                cartCount++;
                
                // Update the text in the header
                if (cartElement) {
                    cartElement.innerHTML = `🛒 Cart ( ${cartCount} )`;
                }

                // Find the dish name (looks for the nearest heading above the button)
                let card = button.parentElement;
                let dishName = card.querySelector('h2, h3')?.innerText || "Delicious Meal";
                
                // Alert confirmation
                alert(`🎉 ${dishName} has been added to your cart!`);
            });
        }
    });