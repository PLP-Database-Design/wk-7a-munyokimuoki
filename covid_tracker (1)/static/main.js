document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("search");
  const countryList = document.querySelectorAll(".country-item");

  searchInput.addEventListener("keyup", function() {
    const filter = searchInput.value.toLowerCase();
    countryList.forEach(item => {
      const countryName = item.textContent.toLowerCase();
      item.style.display = countryName.includes(filter) ? "" : "none";
    });
  });
});
