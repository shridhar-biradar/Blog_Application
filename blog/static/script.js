function getCSRFToken() {
    const token = document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute("content") : "";
}

document.addEventListener("DOMContentLoaded", () => {

    const signupForm = document.getElementById("signup-form");
    if (signupForm) {
        signupForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            const res = await fetch("/api/signup/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                credentials: "same-origin",
                body: JSON.stringify({ username, email, password }),
            });

            const data = await res.json();
            alert(data.message || data.error);
            if (res.ok) window.location.href = "/login/";
        });
    }

    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            const res = await fetch("/api/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                credentials: "same-origin",
                body: JSON.stringify({ email, password }),
            });

            const data = await res.json();
            if (res.ok) {
                window.location.href = "/";
            } else {
                alert(data.error || "Login failed");
            }
        });
    }

    const blogForm = document.getElementById("blog-form");
    if (blogForm) {
        blogForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const title = document.getElementById("title").value;
            const content = document.getElementById("content").value;

            const res = await fetch("/api/create/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                credentials: "same-origin",
                body: JSON.stringify({ title, content }),
            });

            const data = await res.json();
            alert(data.message || data.error);
            if (res.ok) window.location.href = "/";
        });
    }

    const editForm = document.getElementById("edit-blog-form");
    if (editForm) {
        editForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            const title = this.title.value;
            const content = this.content.value;

            const res = await fetch("", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                credentials: "same-origin",
                body: JSON.stringify({ title, content })
            });

            const data = await res.json();
            if (res.ok) {
                alert(data.message || "Blog updated!");
                window.location.href = "/";
            } else {
                alert(data.error || "Update failed");
            }
        });
    }

    const logoutBtn = document.getElementById("logout");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", async (e) => {
            e.preventDefault();
            const res = await fetch("/api/logout/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                credentials: "same-origin",
            });

            const data = await res.json();
            alert(data.message || data.error);
            if (res.ok) window.location.href = "/";
        });
    }

    const deleteButtons = document.querySelectorAll(".delete-blog-btn");
    deleteButtons.forEach(button => {
        button.addEventListener("click", async function (e) {
            e.preventDefault();
            const blogId = this.dataset.blogId;
            if (confirm("Are you sure you want to delete this blog?")) {
                const res = await fetch(`/blog/delete/${blogId}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCSRFToken()
                    },
                    credentials: "same-origin",
                });

                const data = await res.json();
                if (res.ok) {
                    alert("Blog deleted successfully!");
                    window.location.href = "/";
                } else {
                    alert(data.error || "Failed to delete blog.");
                }
            }
        });
    });

});
