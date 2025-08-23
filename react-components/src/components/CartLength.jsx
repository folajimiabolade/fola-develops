import { useEffect, useState } from "react";

function CartLength() {
  const [cartLength, setCartLength] = useState(0);

  useEffect(() => {
    const pageName = document.querySelector('meta[name="page-name"]').getAttribute("content");
    console.log(pageName);
    if (pageName === "store" || pageName === "cart" || "item" || "checkout" || "orders" || "order") {
        document.querySelector("p.item-count").textContent = 2;

    //   fetch("/api/cart/123") // replace 123 with logged-in userId
    //     .then(res => res.json())
    //     .then(data => setCartLength(data.length))
    //     .catch(err => console.error("Error fetching cart:", err));
    }
  }, []); // runs once on mount

  return <div>Cart Items: {cartLength}</div>;
}

export default CartLength;
