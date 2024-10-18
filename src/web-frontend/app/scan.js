window.addEventListener("DOMContentLoaded", () => {
    const websocket = new WebSocket("ws://websocket-server-route-myproject.apps.openshift.com");
  
    document.querySelector(".minus").addEventListener("click", () => {
      websocket.send(JSON.stringify({ action: "minus" }));
    });
  
    document.querySelector(".plus").addEventListener("click", () => {
      websocket.send(JSON.stringify({ action: "plus" }));
    });
  
    websocket.onmessage = ({ data }) => {
      const event = JSON.parse(data);
      switch (event.type) {
        case "value":
          document.querySelector(".value").textContent = event.value;
          break;
        case "users":
          const users = `${event.count} user${event.count == 1 ? "" : "s"}`;
          document.querySelector(".users").textContent = users;
          break;
        default:
          console.error("unsupported event", event);
      }
    };
  });
