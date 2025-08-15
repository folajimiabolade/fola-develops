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
const deleteItem = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"',
    ' class="bi bi-trash-fill toggle-amount" style="opacity: 0.75;" viewBox="0 0 16 16"><path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 ',
    '0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0',
    ' 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1',
    ' .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1',
    ' 0v-7a.5.5 0 0 1 1 0"/></svg>'
].join("");
const reduce = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" ',
    'fill="currentColor" class="bi bi-dash-lg toggle-amount" viewBox="0 0 16 16"><path ',
    'fill-rule="evenodd" d="M2 8a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11A.5.5 0 0 ',
    '1 2 8"/></svg>'
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


// // Convert text version to title case
// function toTitleCase(str) {
//     return str.charAt(0).toUpperCase() + str.slice(1);
// }


 


// // Make each design section show or hide their content, also add their emojis
// function activateDesign(design, emoji) {
//     const business_html1 = '<p class="text design-type"><b>▲ ' + emoji + ' ' + toTitleCase(design) + ' Designs</b></p>';
//     const business_html2 = '<p class="text design-type"><b>▼ ' + emoji + ' ' + toTitleCase(design) + ' Designs</b></p>';
//     $("div." + design).click(() => {
//     $("div." + design + "-designs").toggleClass("hidden");
//     if ($("div." + design + "-designs").hasClass("hidden")) {
//         console.log(true)
//         $("div." + design).html(business_html1);
//     } else {
//         console.log(false)
//         $("div." + design).html(business_html2);
//     }
// })
// }


// activateDesign("business", "💼");
// activateDesign("portfolio", "🗂️");
// activateDesign("blog", "📝");
// activateDesign("personal", "👨🏼‍💼");


// Show or hide the 'Must read' full text when the 'more' or 'less' span element is clicked

// var information = $("div.information").html();
// $("div.information").html(information.slice(0, 440) + '<span class="text must-read"> ...more</span>')

// $("div.information").on("click", "span.must-read", function () {
//     if ($(this).text() === " ...more") {
//         $("div.information").html(information.slice(0, -38) + '<span class="text must-read"> less</span>' + information.slice(-39, -1));    
//     } else if ($(this).text() === " less") {
//         $("div.information").html(information.slice(0, 440) + '<span class="text must-read"> ...more</span>')
//     }
// })


// scroll the page to the list of designs on-click
$("span.touch-designs").click(function () {
    document.querySelector("div.design.business").scrollIntoView({behavior: "smooth"})
})







//  Projects page
$("div.business").click(() => {
    $("div.business-designs").toggleClass("hidden");
    if ($("div.business-designs").hasClass("hidden")) {
        $("div.business").html('<p class="text design-type"><b>▲ 1. 🔐 Authentication System</b></p>');
    } else {
        $("div.business").html('<p class="text design-type"><b>▼ 1. 🔐 Authentication System</b></p>');
    }
});
$("div.portfolio").click(() => {
    $("div.portfolio-designs").toggleClass("hidden");
    if ($("div.portfolio-designs").hasClass("hidden")) {
        $("div.portfolio").html('<p class="text design-type"><b>▲ 2. 📤 Picture Upload Manager</b></p>');
    } else {
        $("div.portfolio").html('<p class="text design-type"><b>▼ 2. 📤 Picture Upload Manager</b></p>');
    }
});
$("div.blog").click(() => {
    $("div.blog-designs").toggleClass("hidden");
    if ($("div.blog-designs").hasClass("hidden")) {
        $("div.blog").html('<p class="text design-type"><b>▲ 3. 🛒 E-commerce Platform (Demo)</b></p>');
    } else {
        $("div.blog").html('<p class="text design-type"><b>▼ 3. 🛒 E-commerce Platform (Demo)</b></p>');
    }
});
$("div.personal").click(() => {
    $("div.personal-designs").toggleClass("hidden");
    if ($("div.personal-designs").hasClass("hidden")) {
        $("div.personal").html('<p class="text design-type"><b>▲ 4. 🤖 AI-Powered Writing Assistant</b></p>');
    } else {
        $("div.personal").html('<p class="text design-type"><b>▼ 4. 🤖 AI-Powered Writing Assistant</b></p>');
    }
});


// Upload section
$("div.upload-house").click(function () {
    $("input.upload-picture").click();
});

$("input.upload-picture").change(function () {
    if ($("input.upload-picture")[0].files.length > 0) {
        const fileName = $("input.upload-picture")[0].files[0].name;
        $("p.file-name").text(fileName);
        $("p.file-name").css("color", "#FF90BB");
    } else {
        $("p.file-name").text("No file chosen");
    }
});


// Upload Item section
$("div.upload-home").click(function () {
    $("input.upload-photo").click();
});

$("input.upload-photo").change(function () {
    if ($("input.upload-photo")[0].files.length > 0) {
        const fileName = $("input.upload-photo")[0].files[0].name;
        $("p.file-title").text(fileName);
        $("p.file-title").css("color", "#FF90BB");
    } else {
        $("p.file-title").text("No file chosen");
    }
});


// Load store
document.addEventListener("DOMContentLoaded", () => {
    const pageName = document.querySelector('meta[name="page-name"]').getAttribute("content");

    if (pageName === "store" || "cart" || "item") {
        fetch("/load-store/api")
        .then(response => response.json())
        .then(function(data)  {
            document.querySelector("p.item-count").textContent = data["cart_length"];
            document.querySelectorAll("a.item-button").forEach(function(item) {
                const itemId = Number(item.getAttribute("data-item-id"));
                $("div.item-button[data-item-id='" + itemId + "']").removeClass("hidden");
                const currentUserId = Number(item.getAttribute("data-current-user-id"));
                data["product_ids"].forEach(content => {
                    const buyerId = data["buyer_ids"][data["product_ids"].indexOf(itemId)]
                    if (buyerId === currentUserId) {
                        var quantity = 0;
                        data["items_ids"].forEach(item => {
                            if (item === itemId) {
                                quantity++;
                            }
                        })
                        $("div.item-button[data-item-id='" + itemId + "']").addClass("hidden");
                        $("p.item-quantity[data-item-id='" + itemId + "']").text(quantity + " item(s) selected");
                        $("div.quantity-buttons[data-item-id='" + itemId + "']").removeClass("hidden");
                    } else {
                        $("div.item-button[data-item-id='" + itemId + "']").removeClass("hidden");
                    }
                })
            });
        });
    }
})


// add-to-cart
document.querySelectorAll("a.item-button").forEach(function(item) {
    item.addEventListener("click", function(event) {
        event.preventDefault()
        const itemId = Number(item.getAttribute("data-item-id"));
        const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch("/add-to-cart/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({
                "item_id": itemId
            })
        })
        .then(response => response.json())
        .then(function(data)  {
            document.querySelector("p.item-count").textContent = data["cart_length"];
            $("div.item-button[data-item-id='" + itemId + "']").addClass("hidden");
            $("p.item-quantity[data-item-id='" + itemId + "']").text(data["quantity"] + " item(s) selected");
            $("div.quantity-buttons[data-item-id='" + itemId + "']").removeClass("hidden");
            })
        });
    })


// Reduce-quantity buttons for store and cart pages
document.querySelectorAll("a.reduce-quantity").forEach(function(item) {
    item.addEventListener("click", function(event) {
        event.preventDefault()
        const itemId = Number(item.getAttribute("data-item-id"));
        const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch("/reduce-quantity/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({
                "item_id": itemId
            })
        })
        .then(response => response.json())
        .then(function(data)  {
            if (data["quantity"] === 0) {
                $("div.quantity-buttons[data-item-id='" + itemId + "']").addClass("hidden");
                $("div.item-button[data-item-id='" + itemId + "']").removeClass("hidden");
                $("div.cart-item[data-item-id='" + itemId + "']").css("display", "none")
            } else if (data["quantity"] === 1) {
                $("a.reduce-amount[data-item-id='" + itemId + "']").html(deleteItem);
                $("p.item-quantity[data-item-id='" + itemId + "']").text(data["quantity"] + " item(s) selected");
                $("p.item-amount[data-item-id='" + itemId + "']").text(data["quantity"]);
            } else{
                $("p.item-quantity[data-item-id='" + itemId + "']").text(data["quantity"] + " item(s) selected");
                $("p.item-amount[data-item-id='" + itemId + "']").text(data["quantity"]);
            }
            document.querySelector("p.item-count").textContent = data["cart_length"];
            document.querySelector("b.total-price").textContent = data["total_price"].toLocaleString('en-NG', { style: 'currency', currency: 'NGN' });
            if (data["cart_length"] === 0) {
                $("a.checkout-button").css("display", "none");
                $("div.total").css("display", "none");
                $("div.empty-cart").removeClass("hidden")
            }
            $("a.checkout-button").text("Proceed to checkout (" + data["cart_length"] + " items[s])")
        })
    })
});


// Increase-quantity buttons for store and cart pages
document.querySelectorAll("a.increase-quantity").forEach(function(item) {
    item.addEventListener("click", function(event) {
        event.preventDefault()
        const itemId = Number(item.getAttribute("data-item-id"));
        const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch("/increase-quantity/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({
                "item_id": itemId
            })
        })
        .then(response => response.json())
        .then(function(data)  {
            $("p.item-quantity[data-item-id='" + itemId + "'], p.item-amount[data-item-id='" + itemId + "']").text(data["quantity"] + " item(s) selected");
            $("p.item-amount[data-item-id='" + itemId + "']").text(data["quantity"]);
            document.querySelector("p.item-count").textContent = data["cart_length"];
            if (data["quantity"] !== 1) {
                $("a.reduce-amount[data-item-id='" + itemId + "']").html(reduce);
            }
            document.querySelector("b.total-price").textContent = data["total_price"].toLocaleString('en-NG', { style: 'currency', currency: 'NGN' });
            $("a.checkout-button").text("Proceed to checkout (" + data["cart_length"] + " items[s])")
        })
    })
});


// Make every item image on the store home page a button that links to it's information
document.querySelectorAll("img.item-image").forEach(function(item) {
    item.addEventListener("click", function() {
        const itemId = item.getAttribute("data-item-id");
        document.querySelector("a.item-information.id-" + itemId).click();
    })
})


// Load cart page
document.addEventListener("DOMContentLoaded", () => {
    const pageName = document.querySelector('meta[name="page-name"]').getAttribute("content");

    if (pageName === "cart") {
        document.querySelectorAll("a.reduce-amount").forEach(item => {
            const quantity = Number(item.getAttribute("data-quantity"));
            if (quantity === 1) {
                item.innerHTML = deleteItem;
            }
        })
    }
});


// Delete item from cart
document.querySelectorAll("a.delete-item").forEach(item => {
    item.addEventListener("click", function(event) {
        event.preventDefault()
        const itemId = Number(item.getAttribute("data-item-id"));
        const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch("/delete-item/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": token
            },
            body: JSON.stringify({
                "item_id": itemId
            })
        })
        .then(response => response.json())
        .then(function(data)  {
            $("div.cart-item[data-item-id='" + itemId + "']").css("display", "none");
            if (data["cart_length"] === 0) {
                $("a.checkout-button").css("display", "none");
                $("div.total").css("display", "none");
                $("div.empty-cart").removeClass("hidden")
            }
        })
    })
});


// Reduce count on 'Item' page
document.querySelector("a.reduce-count").addEventListener("click", function(event) {
    event.preventDefault();
    const itemId = Number(document.querySelector("a.reduce-count").getAttribute("data-item-id"));
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch("/reduce-quantity/api", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token
        },
        body: JSON.stringify({
            "item_id": itemId
        })
    })
    .then(response => response.json())
    .then(data => {
            if (data["quantity"] === 0) {
                $("div.count-buttons[data-item-id='" + itemId + "']").addClass("hidden");
                $("a.add-item[data-item-id='" + itemId + "']").removeClass("hidden");
            } else{
                $("p.item-size[data-item-id='" + itemId + "']").text(data["quantity"]);
            }
            document.querySelector("p.item-count").textContent = data["cart_length"];
    });
})


// Increase count on 'Item' page
document.querySelector("a.increase-count").addEventListener("click", function(event) {
    event.preventDefault()
    const itemId = Number(document.querySelector("a.increase-count").getAttribute("data-item-id"));
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch("/increase-quantity/api", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token
        },
        body: JSON.stringify({
            "item_id": itemId
        })
    })
    .then(response => response.json())
    .then(function(data)  {
        $("p.item-size[data-item-id='" + itemId + "']").text(data["quantity"]);
        document.querySelector("p.item-count").textContent = data["cart_length"];
    })
});


// Add to cart from 'Item' page
document.querySelector("a.add-item").addEventListener("click", function(event) {
    event.preventDefault()
    const itemId = Number(document.querySelector("a.add-item").getAttribute("data-item-id"));
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch("/add-to-trolley/api", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": token
        },
        body: JSON.stringify({
            "item_id": itemId
        })
    })
    .then(response => response.json())
    .then(function(data)  {
        $("a.add-item[data-item-id='" + itemId + "']").addClass("hidden");
        $("p.item-size[data-item-id='" + itemId + "']").text(data["quantity"]);
        $("div.count-buttons[data-item-id='" + itemId + "']").removeClass("hidden");
        document.querySelector("p.item-count").textContent = data["cart_length"];
    })
});




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
