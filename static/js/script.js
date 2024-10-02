// Detect hover over the hover zone and open the side panel
document.getElementById("hoverZone").addEventListener("mouseenter", function() {
    openMenu(); // Open the side panel when hovering
});

// Detect when the mouse leaves the side panel area to close it
document.getElementById("sidePanel").addEventListener("mouseleave", function() {
    closeMenu(); // Close the side panel when cursor leaves the panel
});

// Function to open the side panel
function openMenu() {
    document.body.classList.add("open-panel");
}

// Function to close the side panel
function closeMenu() {
    document.body.classList.remove("open-panel");
}
