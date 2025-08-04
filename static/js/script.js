const openedIcon = [
            '<path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 ',
            '.708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 ',
            '0 0 1-.708-.708L7.293 8z"/> Menula'
        ].join("");
const closedIcon = [
            '<path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 ',
            '.5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 ',
            '0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5',
            '0 0 1-.5-.5"/> Menule'
        ].join("");

/*
Show and hide the navigation bar whenever the 'Menu' button is clicked on portrait mode,
do not hide the navigation bar on landscape mode
*/
// Check for clicks on the 'Menu' button
$("button.menu").click(function () {
    // Check if the navigation bar is showing(display: flex) or if it's hidden(display: none)
    // and change the 'Menu' button's icon accordingly
    if ($("div.links-container").css("display") === "flex") {
        $("svg.menu-icon").html(closedIcon);
    } else {
        $("svg.menu-icon").html(openedIcon);
    }
    // Animate the navigation bar's show/hide process to slide out/in
    $("div.links-container").slideToggle();
})


// If the page orientation changes from landscape to portrait mode
// and the navigation bar is not hidden, hide the navigation bar, and
// if the page orientation changes from portrait to landscape mode and the
// navigation bar is hidden, unhide the navigation bar
var screenOrientation = window.matchMedia("(orientation: portrait)");
screenOrientation.addEventListener("change", detectChange)


function detectChange(portraitState) {
    if (portraitState.matches) {
        $("div.links-container").css("display", "none");
        $("svg.menu-icon").html(closedIcon);
    } else {
        if ($("div.links-container").css("display") === "none") {
            $("div.links-container").css("display", "flex");
        }
    }
}


detectChange(screenOrientation);


// Fade the hero in.
//window.onload(function () {
//    $("div.hero-prompt").fadeOut();
//})

$(document).ready(function () {
    setInterval(function () {$(".hero-body, .hero-actions, h2.home-testifies, div.home-testifies, a.more-testimonies").fadeIn(500)}, 500)
  });



// Show navigation bar only when scrolling up if the page is not a user page
if (this.document.querySelector("div.user-page")) { // if it is a user page
    $("div.navigation-container").css("position", "static")
    $("div.navigation-container").css("top", "auto")
} else { // if it not is a user page
    var currentScroll = window.scrollY || document.documentElement.scrollTop;
    window.addEventListener("scroll", function () {
        var lastScroll = currentScroll;
        currentScroll = window.scrollY || document.documentElement.scrollTop;
        if (currentScroll < 0) { // Default all negative values to 0. 
            currentScroll = 0;
        }
        if (currentScroll > lastScroll) {
            $("div.navigation-container").slideUp(333);
        } else if (currentScroll < lastScroll) {
            $("div.navigation-container").slideDown(333);
        }

////        Transparent navbar effect
//        if (currentScroll === 0) {
//            if (window.innerWidth > window.innerHeight) {
//              $("div.navigation-container").css("background", "transparent");
//            }
//        } else {
//            $("div.navigation-container").css("background", "#2b3035");
//        }
    })
}


// Convert text version to title case
function toTitleCase(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


// Make each design section show or hide their content, also add their emojis
function activateDesign(design, emoji) {
    const business_html1 = '<p class="text design-type"><b>▲ ' + emoji + ' ' + toTitleCase(design) + ' Designs</b></p>';
    const business_html2 = '<p class="text design-type"><b>▼ ' + emoji + ' ' + toTitleCase(design) + ' Designs</b></p>';
    $("div." + design).click(() => {
    $("div." + design + "-designs").toggleClass("hidden");
    if ($("div." + design + "-designs").hasClass("hidden")) {
        console.log(true)
        $("div." + design).html(business_html1);
    } else {
        console.log(false)
        $("div." + design).html(business_html2);
    }
})
}


activateDesign("business", "💼");
activateDesign("portfolio", "🗂️");
activateDesign("blog", "📝");
activateDesign("personal", "👨🏼‍💼");


// Show or hide the 'Must read' full text when the 'more' or 'less' span element is clicked

var information = $("div.information").html();
$("div.information").html(information.slice(0, 440) + '<span class="text must-read"> ...more</span>')

$("div.information").on("click", "span.must-read", function () {
    if ($(this).text() === " ...more") {
        $("div.information").html(information.slice(0, -38) + '<span class="text must-read"> less</span>' + information.slice(-39, -1));    
    } else if ($(this).text() === " less") {
        $("div.information").html(information.slice(0, 440) + '<span class="text must-read"> ...more</span>')
    }
})


// scroll the page to the list of designs on-click
$("span.touch-designs").click(function () {
    document.querySelector("div.design.business").scrollIntoView({behavior: "smooth"})
})




// // Get data from the database by fetching data from the Flask server
//$(".betan").click(function () {
//    fetch("http://127.0.0.1:5000/flow/api").then(function (response) {
//        return response.json();
//    }).then(function (data) {
//        $(".details-shower").html([
//            ("Your first name is " + data["first name"] + ", your last name "),
//            ("is " + data["last name"] + ", and your email is " + data["email"] + ", "),
//            ("Your is image is " + "<img width='500vw' height='500vw' src='" + data["picture url"] + "'>" )
//        ].join(""));
//    })
//})
