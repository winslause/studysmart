$(document).ready(function() {
  // ===== SPIDER-WEB & GALAXY BACKGROUND =====
  const canvas = document.getElementById('spider-web-bg');
  const ctx = canvas.getContext('2d');
  let nodes = [];
  let stars = [];
  let isWebEnabled = true;

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  function createNodes() {
    nodes = [];
    const nodeCount = 50;
    for (let i = 0; i < nodeCount; i++) {
      nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 1.5,
        vy: (Math.random() - 0.5) * 1.5,
        radius: 3
      });
    }
  }

  function createStars() {
    stars = [];
    const starCount = 200;
    for (let i = 0; i < starCount; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: 0.5 + Math.random() * 1.5,
        opacity: 0.4 + Math.random() * 0.6
      });
    }
  }
  createNodes();
  createStars();

  function drawBackground() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw nebula-like gradient
    const gradient = ctx.createRadialGradient(
      canvas.width / 2, canvas.height / 2, 100,
      canvas.width / 2, canvas.height / 2, Math.max(canvas.width, canvas.height)
    );
    gradient.addColorStop(0, 'rgba(0, 242, 254, 0.1)');
    gradient.addColorStop(0.5, 'rgba(121, 40, 202, 0.05)');
    gradient.addColorStop(1, 'rgba(15, 15, 26, 0)');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw stars
    ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
    stars.forEach(star => {
      ctx.globalAlpha = star.opacity;
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1;
    });

    // Draw web lines
    ctx.strokeStyle = '#00f2fe';
    ctx.lineWidth = 0.6;
    ctx.shadowBlur = 12;
    ctx.shadowColor = 'rgba(0, 242, 254, 0.6)';
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dist = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.stroke();
        }
      }
    }

    // Draw web nodes
    ctx.shadowBlur = 18;
    ctx.shadowColor = 'rgba(255, 45, 117, 0.8)';
    ctx.fillStyle = '#ff2d75';
    nodes.forEach(node => {
      ctx.beginPath();
      ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
      ctx.fill();
    });
    ctx.shadowBlur = 0;
  }

  function updateNodes() {
    nodes.forEach(node => {
      node.x += node.vx;
      node.y += node.vy;
      if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
      if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
    });
  }

  function updateStars() {
    stars.forEach(star => {
      star.opacity = 0.4 + Math.sin(Date.now() * 0.002 + star.x) * 0.3;
    });
  }

  function animateBackground() {
    if (isWebEnabled) {
      updateNodes();
      updateStars();
      drawBackground();
    }
    requestAnimationFrame(animateBackground);
  }
  animateBackground();

  $('#toggle-web').click(function() {
    isWebEnabled = !isWebEnabled;
    canvas.style.display = isWebEnabled ? 'block' : 'none';
    $(this).html(`<i class="fas fa-atom"></i> ${isWebEnabled ? 'Hide Web' : 'Show Web'}`);
  });

  // ===== MATRIX EFFECT =====
  $('.btn-outline-light').click(function(e) {
    e.preventDefault();
    launchMatrixEffect();
  });

  function launchMatrixEffect() {
    const overlay = $('#matrix-overlay');
    overlay.fadeIn(500);
    $('#skip-matrix').fadeIn();

    for (let i = 0; i < 250; i++) {
      createMatrixChar(overlay);
    }

    for (let i = 0; i < 25; i++) {
      createMatrixCircle(overlay);
    }

    const matrixTimeout = setTimeout(() => {
      closeMatrixEffect();
    }, 8000);

    $('#skip-matrix').off('click').on('click', function() {
      clearTimeout(matrixTimeout);
      closeMatrixEffect();
    });
  }

  function createMatrixChar(container) {
    const char = Math.random() > 0.5 ? '0' : '1';
    const $char = $(`<div class="matrix-char">${char}</div>`);

    const left = Math.random() * 100;
    const delay = Math.random() * 5;
    const duration = 3 + Math.random() * 4;

    $char.css({
      left: `${left}%`,
      top: '100%',
      animation: `matrix-rise ${duration}s linear ${delay}s infinite`,
      fontSize: `${12 + Math.random() * 10}px`,
      opacity: 0.5 + Math.random() * 0.5
    });

    container.append($char);
  }

  function createMatrixCircle(container) {
    const size = 20 + Math.random() * 100;
    const $circle = $('<div class="matrix-circle"></div>');

    $card.css({
      width: `${size}px`,
      height: `${size}px`,
      left: `${Math.random() * 100}%`,
      top: `${Math.random() * 100}%`,
      animation: `pulse ${2 + Math.random() * 3}s ease-in-out infinite`,
      borderWidth: `${Math.random() * 3}px`
    });

    container.append($circle);
  }

  function closeMatrixEffect() {
    $('#matrix-overlay').fadeOut(500, function() {
      $(this).empty();
    });
    $('#skip-matrix').fadeOut();
  }

  // ===== VOICE COMMANDS =====
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    $('#voice-search').click(function() {
      recognition.start();
      $(this).addClass('listening').html('<i class="fas fa-microphone"></i> Listening...');
    });
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript.toLowerCase();
      $('#voice-search').removeClass('listening').html('<i class="fas fa-microphone"></i> Voice AI');
      if (transcript.includes('services')) window.location.href = '{% url "services" %}';
      else if (transcript.includes('about')) window.location.href = '/about/';
      else if (transcript.includes('register')) window.location.href = '{% url "register" %}';
      else if (transcript.includes('login')) window.location.href = '{% url "login" %}';
    };
  } else {
    $('#voice-search').hide();
  }

  // ===== GSAP ANIMATIONS =====
  gsap.registerPlugin(ScrollTrigger);
  gsap.from('.navbar', {
    opacity: 0,
    y: 0,
    duration: 0.4,
    onComplete: function() {
      $('.navbar').css({ opacity: 1, visibility: 'visible', transform: 'none' });
    }
  });
  gsap.from('.nav-link', {
    opacity: 0,
    y: 0,
    stagger: 0.1,
    duration: 0.5,
    delay: 0.8,
    onComplete: function() {
      $('.nav-link').css({ opacity: 1, visibility: 'visible', transform: 'none' });
    }
  });
  gsap.from('.btn-wens', {
    opacity: 0,
    x: 20,
    stagger: 0.1,
    duration: 0.5,
    delay: 1,
    onComplete: function() {
      $('.btn-wens').css({ opacity: 1, visibility: 'visible', transform: 'none' });
    }
  });
  gsap.from('.footer', {
    opacity: 0,
    y: 50,
    duration: 0.8,
    scrollTrigger: { trigger: '.footer', start: 'top 90%' }
  });

  // Debug toggler
  $('.navbar-toggler').on('click', function() {
    console.log('Toggler clicked, aria-expanded:', $(this).attr('aria-expanded'));
    console.log('NavbarNav classes:', $('#navbarNav').attr('class'));
  });

  $('.navbar-collapse').on('show.bs.collapse', function() {
    console.log('Collapse showing');
    $(this).css({ opacity: 1, visibility: 'visible' });
  }).on('hide.bs.collapse', function() {
    console.log('Collapse hiding');
  });
});