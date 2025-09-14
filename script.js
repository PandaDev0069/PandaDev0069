// Smooth scrolling
function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: 'smooth'
  });
}

// Add smooth scrolling to all navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Navbar background on scroll
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (window.scrollY > 100) {
    navbar.style.background = 'rgba(0, 0, 0, 0.8)';
  } else {
    navbar.style.background = 'rgba(255, 255, 255, 0.1)';
  }
});

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
  section.style.opacity = '0';
  section.style.transform = 'translateY(30px)';
  section.style.transition = 'all 0.6s ease';
  observer.observe(section);
});

// Hide scroll indicator after scrolling
window.addEventListener('scroll', () => {
  const scrollIndicator = document.querySelector('.scroll-indicator');
  if (window.scrollY > 100) {
    scrollIndicator.style.opacity = '0';
    scrollIndicator.style.pointerEvents = 'none';
  } else {
    scrollIndicator.style.opacity = '1';
    scrollIndicator.style.pointerEvents = 'auto';
  }
});

// Add particle interaction
document.addEventListener('mousemove', (e) => {
  const particles = document.querySelectorAll('.particle');
  const x = e.clientX / window.innerWidth;
  const y = e.clientY / window.innerHeight;
  
  particles.forEach((particle, index) => {
    const speed = (index + 1) * 0.01;
    const xPos = (x - 0.5) * speed * 100;
    const yPos = (y - 0.5) * speed * 100;
    particle.style.transform = `translate(${xPos}px, ${yPos}px)`;
  });
});