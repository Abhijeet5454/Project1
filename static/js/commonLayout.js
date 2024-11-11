document.addEventListener("DOMContentLoaded", function() {
    const leftPanel = document.getElementById('left-panel');
    const body = document.body;

    // Show or hide left panel box when hover over
    leftPanel.addEventListener('mouseenter', function() {
        body.classList.add('hover-active');
    });
    
    leftPanel.addEventListener('mouseleave', function() {
        body.classList.remove('hover-active');
    });

});
