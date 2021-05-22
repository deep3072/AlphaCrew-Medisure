var menu = document.getElementById("menubar");
      var sidenav = document.getElementById("sidenav");
      sidenav.style.width = "0px";
      menu.onclick = function () {
        if (sidenav.style.width == "0px") {
          sidenav.style.width = "250px";
          menu.src = "https://i.ibb.co/mRYdnxH/cross.png";
        } else {
          sidenav.style.width = "0px";
          menu.src = "https://i.ibb.co/k5Dyz1b/download.png";
        }
      };