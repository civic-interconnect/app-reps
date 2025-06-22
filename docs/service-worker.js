const CACHE_NAME = "ci-reps-cache-v1";
const urlsToCache = [
  "/app-reps/",
  "/app-reps/index.html",
  "/app-reps/script.js",
  "/app-reps/style.css",
  "/app-reps/manifest.json",
  "/app-reps/components/ci-rep.js",
  "/app-reps/components/ci-footer.js",
  "/app-reps/components/ci-header.js",
  "/app-reps/status.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      )
    )
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).catch(() => {
        return new Response("Offline and not cached", {
          status: 503,
          statusText: "Service Unavailable",
          headers: { "Content-Type": "text/plain" }
        });
      });
    })
  );
});
