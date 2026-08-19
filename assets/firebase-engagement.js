import { initializeApp } from "https://www.gstatic.com/firebasejs/11.10.0/firebase-app.js";
import {
  getAuth,
  onAuthStateChanged,
  signInAnonymously,
} from "https://www.gstatic.com/firebasejs/11.10.0/firebase-auth.js";
import {
  addDoc,
  collection,
  deleteDoc,
  doc,
  getCountFromServer,
  getDoc,
  getFirestore,
  onSnapshot,
  orderBy,
  query,
  serverTimestamp,
  setDoc,
} from "https://www.gstatic.com/firebasejs/11.10.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyChVJyJ2SwdT7P5jqyfe_OkAzgWTq8gDBo",
  authDomain: "ghif-lab.firebaseapp.com",
  projectId: "ghif-lab",
  storageBucket: "ghif-lab.firebasestorage.app",
  messagingSenderId: "437745445601",
  appId: "1:437745445601:web:fa7b81b0e3d5e4149665a0",
  measurementId: "G-V9HWHBEVSV",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const slug = window.location.pathname
  .replace(/^\/+|\/+$/g, "")
  .split("/")
  .slice(1)
  .join("/");

if (!slug || !window.location.pathname.startsWith("/posts/")) {
  // Engagement controls are intentionally limited to article pages.
} else {
  const articleRef = doc(db, "articles", slug);
  const likesRef = collection(articleRef, "likes");
  const commentsRef = collection(articleRef, "comments");
  const commentsQuery = query(commentsRef, orderBy("createdAt", "desc"));
  const mount = document.createElement("section");
  mount.className = "article-engagement";
  mount.setAttribute("aria-labelledby", "engagement-title");
  mount.innerHTML = `
    <h2 id="engagement-title">Join the discussion</h2>
    <div class="engagement-actions">
      <button class="engagement-like" type="button" disabled>♡ Like <span>0</span></button>
    </div>
    <p class="engagement-status" role="status">Loading engagement…</p>
    <form class="engagement-form" hidden>
      <label for="engagement-comment">Your comment</label>
      <textarea id="engagement-comment" maxlength="2000" required placeholder="Share a thought or question…"></textarea>
      <button type="submit">Post comment</button>
    </form>
    <div class="engagement-comments" aria-live="polite"></div>
  `;
  document.querySelector("#quarto-document-content")?.append(mount);

  const likeButton = mount.querySelector(".engagement-like");
  const form = mount.querySelector(".engagement-form");
  const status = mount.querySelector(".engagement-status");
  const commentsList = mount.querySelector(".engagement-comments");
  let currentUser = null;
  let unsubscribeComments = null;

  const escapeText = (value) => {
    const span = document.createElement("span");
    span.textContent = value || "";
    return span.innerHTML;
  };

  const refreshLikes = async () => {
    const count = await getCountFromServer(likesRef);
    likeButton.querySelector("span").textContent = count.data().count;
    likeButton.disabled = !currentUser;
    if (currentUser) {
      const like = await getDoc(doc(likesRef, currentUser.uid));
      likeButton.classList.toggle("is-liked", like.exists());
      likeButton.firstChild.textContent = like.exists() ? "♥ Unlike " : "♡ Like ";
    }
  };

  const renderComments = (snapshot) => {
    commentsList.replaceChildren();
    if (snapshot.empty) {
      commentsList.innerHTML = "<p class=\"engagement-empty\">Be the first to comment.</p>";
      return;
    }
    snapshot.forEach((commentSnapshot) => {
      const comment = commentSnapshot.data();
      const item = document.createElement("article");
      item.className = "engagement-comment";
      const date = comment.createdAt?.toDate?.().toLocaleDateString(undefined, {
        year: "numeric", month: "short", day: "numeric",
      }) || "Just now";
      item.innerHTML = `
        <header><strong>${escapeText(comment.authorName || "Reader")}</strong><time>${date}</time></header>
        <p></p>
      `;
      item.querySelector("p").textContent = comment.body;
      commentsList.append(item);
    });
  };

  const setSignedInState = async (user) => {
    currentUser = user;
    const signedIn = Boolean(user);
    form.hidden = !signedIn;
    status.textContent = signedIn
      ? `Participating as ${user.displayName || user.email || "Anonymous Reader"}.`
      : "Connecting anonymously…";
    try {
      await refreshLikes();
    } catch (error) {
      status.textContent = `Firestore error: ${error.code || error.message}`;
    }
  };

  likeButton.addEventListener("click", async () => {
    if (!currentUser) return;
    const likeRef = doc(likesRef, currentUser.uid);
    const like = await getDoc(likeRef);
    if (like.exists()) {
      await deleteDoc(likeRef);
    } else {
      await setDoc(likeRef, { createdAt: serverTimestamp() });
    }
    try {
      await refreshLikes();
    } catch (error) {
      status.textContent = `Firestore error: ${error.code || error.message}`;
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const textarea = form.querySelector("textarea");
    const body = textarea.value.trim();
    if (!body || !currentUser) return;
    try {
      await addDoc(commentsRef, {
        authorId: currentUser.uid,
        authorName: currentUser.displayName || currentUser.email || "Reader",
        body,
        createdAt: serverTimestamp(),
      });
      textarea.value = "";
      status.textContent = "Comment posted.";
    } catch (error) {
      status.textContent = `Comment error: ${error.code || error.message}`;
    }
  });

  onAuthStateChanged(auth, setSignedInState);
  signInAnonymously(auth).catch((error) => {
    status.textContent = `Anonymous sign-in failed: ${error.code || error.message}`;
  });
  getCountFromServer(likesRef).then(refreshLikes).catch((error) => {
    status.textContent = `Firestore error: ${error.code || error.message}`;
  });
  unsubscribeComments = onSnapshot(commentsQuery, renderComments, (error) => {
    commentsList.innerHTML = "<p class=\"engagement-empty\">Comments are temporarily unavailable.</p>";
    status.textContent = `Comments error: ${error.code || error.message}`;
  });
}
