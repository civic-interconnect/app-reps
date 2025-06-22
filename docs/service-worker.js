const CACHE_NAME = "ci-reps-cache-v1";
const urlsToCache = [
  "./",
  "./index.html",
  "./script.js",
  "./style.css",
  "./manifest.json",
  "./components/ci-rep.js",
  "./components/ci-footer.js",
  "./components/ci-header.js",
  "./status.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then(
      (response) => response || fetch(event.request)
    )
  );
});
