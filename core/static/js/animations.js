gsap.registerPlugin(ScrollTrigger);

gsap.from(".navbar", {
  y: -100,
  opacity: 0,
  duration: 0.8,
  ease: "power2.out",
});

gsap.from(".carousel-caption", {
  y: 50,
  opacity: 0,
  duration: 0.8,
  ease: "power2.out",
  stagger: 0.2,
  scrollTrigger: {
    trigger: ".carousel",
    start: "top 80%",
  },
});

gsap.from(".footer", {
  y: 50,
  opacity: 0,
  duration: 0.8,
  ease: "power2.out",
  scrollTrigger: {
    trigger: ".footer",
    start: "top 90%",
  },
});