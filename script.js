async function loadData(url, containerId, type, searchId) {
  try {
    const response = await fetch(url);
    let data = await response.json();
    const container = document.getElementById(containerId);
    const searchInput = document.getElementById(searchId);

    function render(items) {
      container.innerHTML = "";
      items.forEach((item, idx) => {
        const div = document.createElement("div");
        div.className = "blog-post";

        if (type === "pta") {
          div.innerHTML = `
            <h3>Abstrak #${idx + 1}</h3>
            <p>${item.abstrak || item["Isi_Token"]?.join(" ")}</p>
          `;
        } else if (type === "berita") {
          div.innerHTML = `
            <h3>${item["Judul Berita"] || "Tanpa Judul"}</h3>
            <p>${item["Isi_Token"]?.join(" ") || ""}</p>
          `;
        }
        container.appendChild(div);
      });
    }

    // render awal
    render(data);

    // filter saat ketik pencarian
    if (searchInput) {
      searchInput.addEventListener("input", () => {
        const keyword = searchInput.value.toLowerCase();
        const filtered = data.filter(item => {
          return JSON.stringify(item).toLowerCase().includes(keyword);
        });
        render(filtered);
      });
    }
  } catch (err) {
    console.error("Gagal load data:", err);
  }
}

// jalankan sesuai halaman
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("pta-container")) {
    loadData("data/pta.json", "pta-container", "pta", "search-pta");
  }
  if (document.getElementById("berita-container")) {
    loadData("data/berita.json", "berita-container", "berita", "search-berita");
  }
});
