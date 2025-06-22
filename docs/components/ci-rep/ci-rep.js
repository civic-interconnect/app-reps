// File: components/ci-rep/ci-rep.js
const styleURL = new URL("./ci-rep.css", import.meta.url);
const coreFields = ["version", "schema_source", "action_status"];

class CiRep extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this._repData = null; // Hold rep data if set early
  }

  async connectedCallback() {
    const style = await fetch(styleURL).then((res) => res.text());

    this.shadowRoot.innerHTML = `
      <style>${style}</style>
      <article class="rep-card"></article>
    `;

    this.container = this.shadowRoot.querySelector(".rep-card");

    // Now render if data was set before connectedCallback finished
    if (this._repData) {
      this.render(this._repData);
    }

    const updateTheme = () => {
      const theme = document.body.dataset.theme || "light";
      this.setAttribute("data-theme", theme);
    };
    const observer = new MutationObserver(updateTheme);
    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });
    updateTheme();
    this._themeObserver = observer;
  }

  set data(rep) {
    if (this.container) {
      this.render(rep);
    } else {
      this._repData = rep; // Save until connectedCallback runs
    }
  }

  render(rep) {
    const status = (rep.action_status || "").toLowerCase();
    const statusClass =
      status.includes("success") || status.includes("passed")
        ? "status-ok"
        : status.includes("pending")
        ? "status-warn"
        : "status-bad";

    const safeField = (field) =>
      rep[field] !== undefined ? rep[field] : "—";

    const extraFields = Object.entries(rep)
      .filter(
        ([key]) =>
          !["name", "repo", "last_commit", ...coreFields, "report_url"].includes(key)
      )
      .map(
        ([key, value]) =>
          `<p><strong>${formatLabel(key)}:</strong> ${value}</p>`
      )
      .join("\n");

    this.container.innerHTML = `
      <header>
        <h2><a href="${safeField("repo")}" target="_blank" rel="noopener">
          ${safeField("name")}</a></h2>
        <small>Last commit: ${safeField("last_commit")}</small>
      </header>
      <section>
        <p><strong>Version:</strong> ${safeField("version")}</p>
        <p><strong>Schema Source:</strong> ${safeField("schema_source")}</p>
        <p><strong>Status:</strong> <span class="${statusClass}">${safeField("action_status")}</span></p>
        ${extraFields}
      </section>
    `;
  }
}

function formatLabel(key) {
  return key.replace(/_/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
}

customElements.define("ci-rep", CiRep);
