
document.addEventListener('DOMContentLoaded', () =>{
  const searchForm = document.getElementById('recipe-search-form');
  const showSearchButton = document.getElementById('show-search-button');

  showSearchButton.addEventListener('click', () =>{
    if (searchForm.style.display === 'none') {
      searchForm.style.display = 'block';
      showSearchButton.innerText = 'Hide Search Form';
    } else {
      searchForm.style.display = 'none';
      showSearchButton.innerText = 'Search For Recipes';
      
    }
  });
});