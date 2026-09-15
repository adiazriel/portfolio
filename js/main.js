(function () {
  "use strict";

  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // TODO: theme toggle, mobile nav, scroll effects, etc. as the site grows
})();
