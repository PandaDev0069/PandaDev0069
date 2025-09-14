/**
 * Futuristic Portfolio - Enhanced Interactive Features
 * This file contains additional futuristic effects and interactions
 */

// Enhanced particle system with dynamic colors
class FuturisticParticleSystem {
  constructor() {
    this.particles = [];
    this.colors = ['#667eea', '#764ba2', '#ff6b6b', '#ee5a24', '#a8edea'];
    this.init();
  }

  init() {
    // Enhanced particle interactions
    this.createGlowEffects();
    this.addHoverAnimations();
    this.initTypingEffect();
  }

  createGlowEffects() {
    // Add dynamic glow to project cards
    document.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('mouseenter', (e) => {
        e.target.style.boxShadow = '0 0 30px rgba(102, 126, 234, 0.5), 0 0 60px rgba(102, 126, 234, 0.3)';
        e.target.style.borderColor = 'rgba(102, 126, 234, 0.8)';
      });

      card.addEventListener('mouseleave', (e) => {
        e.target.style.boxShadow = '';
        e.target.style.borderColor = 'rgba(255, 255, 255, 0.2)';
      });
    });
  }

  addHoverAnimations() {
    // Enhanced skill item animations
    document.querySelectorAll('.skill-item').forEach(item => {
      item.addEventListener('mouseenter', (e) => {
        e.target.style.background = `linear-gradient(45deg, ${this.getRandomColor()}, ${this.getRandomColor()})`;
        e.target.style.transform = 'translateY(-15px) rotate(5deg) scale(1.05)';
      });

      item.addEventListener('mouseleave', (e) => {
        e.target.style.background = 'rgba(255, 255, 255, 0.1)';
        e.target.style.transform = '';
      });
    });
  }

  getRandomColor() {
    return this.colors[Math.floor(Math.random() * this.colors.length)];
  }

  initTypingEffect() {
    // Add typing effect to hero subtitle
    const subtitle = document.querySelector('.hero-subtitle');
    const originalText = subtitle.textContent;
    subtitle.textContent = '';
    
    let i = 0;
    const typeWriter = () => {
      if (i < originalText.length) {
        subtitle.textContent += originalText.charAt(i);
        i++;
        setTimeout(typeWriter, 100);
      }
    };
    
    // Start typing effect after a delay
    setTimeout(typeWriter, 1000);
  }
}

// Enhanced scroll effects
class FuturisticScrollEffects {
  constructor() {
    this.init();
  }

  init() {
    this.addParallaxEffect();
    this.addProgressIndicator();
  }

  addParallaxEffect() {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const parallax = document.querySelector('.hero');
      
      if (parallax) {
        const speed = scrolled * 0.5;
        parallax.style.transform = `translateY(${speed}px)`;
      }
    });
  }

  addProgressIndicator() {
    // Create scroll progress bar
    const progressBar = document.createElement('div');
    progressBar.style.position = 'fixed';
    progressBar.style.top = '0';
    progressBar.style.left = '0';
    progressBar.style.width = '0%';
    progressBar.style.height = '3px';
    progressBar.style.background = 'linear-gradient(45deg, #ff6b6b, #ee5a24)';
    progressBar.style.zIndex = '10000';
    progressBar.style.transition = 'width 0.3s ease';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      progressBar.style.width = scrolled + '%';
    });
  }
}

// Initialize futuristic effects when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const particleSystem = new FuturisticParticleSystem();
  const scrollEffects = new FuturisticScrollEffects();
  
  console.log('🚀 Futuristic Portfolio Effects Activated!');
});