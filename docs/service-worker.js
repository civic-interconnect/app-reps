const CACHE_NAME = "ci-reps-cache-v1";
const BASE_PATH = "/app-reps/";
const urlsToCache = [
  `${BASE_PATH}`,
  `${BASE_PATH}index.html`,
  `${BASE_PATH}index.js`,
  `${BASE_PATH}style.css`,
  `${BASE_PATH}manifest.json`,
  `${BASE_PATH}components/ci-rep.js`,
  `${BASE_PATH}status.json`,
  "https://civic-interconnect.github.io/app-core/components/ci-header/ci-header.js",
  "https://civic-interconnect.github.io/app-core/components/ci-footer/ci-footer.js",
  "https://civic-interconnect.github.io/app-core/styles/tokens.css",
  "https://civic-interconnect.github.io/app-core/styles/themes.css",
  "https://civic-interconnect.github.io/app-core/styles/base.css",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((cacheNames) =>
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
      return (
        response ||
        fetch(event.request).catch(() => {
          return new Response("Offline and not cached", {
            status: 503,
            statusText: "Service Unavailable",
            headers: { "Content-Type": "text/plain" },
          });
        })
      );
    })
  );
});
