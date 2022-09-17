let logoutBtn = document.getElementById("logout")
let guideidValue = localStorage.getItem("id");
let dayInput = document.getElementById("days");
let priceInput = document.getElementById("price");
let addBtn = document.getElementById("addButton");
let titleInput = document.getElementById("title");
let loginErrorMessageDiv = document.getElementById('login-error-message');
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";

logoutBtn.addEventListener('click', logout)
document.addEventListener("DOMContentLoaded", loginstatus);
addBtn.addEventListener('click', add_tour)

function loginstatus() {
  if (localStorage.getItem("role") == "user") {
    window.location.href = "/tours.html";
  }
  if (localStorage.getItem("role") != "guide") {
    window.location.href = "/tours.html"
  }
}

async function logout() {
  try {
    let res = await fetch(`http://${devDomain}:8080/logout`, {
      'method': 'POST',
    })
    console.log(res);
    if (res.status == 200) {
      localStorage.clear();
      window.alert("Logout Successful");
      window.location.href = "/index.html";
    }
  } catch (err) {
    console.log(err.message)
  }
}

async function add_tour() {
  loginErrorMessageDiv.innerHTML = "";
  let selected = document.querySelectorAll('#stops option:checked');
  let routeInput = Array.from(selected).map(el => el.value);

  let res = await fetch(`http://${devDomain}:8080/tour/add`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "guide_id": guideidValue,
      "day": dayInput.value,
      "pois": routeInput,
      "price": priceInput.value,
      "title": titleInput.value
    }),
  })
  if (res.status == 200) {
    alert("Tour Added")
    window.location.href = "/mytours.html"
  } else if (res.status == 400) {
    let data = await res.json();
    let errorElement = document.createElement('p');
    errorElement.innerHTML = data.message;
    errorElement.style.color = 'red';
    errorElement.style.fontWeight = 'bold';
    loginErrorMessageDiv.appendChild(errorElement);
  }

}

var style = document.createElement('style');
style.setAttribute("id", "multiselect_dropdown_styles");

document.head.appendChild(style);

function MultiselectDropdown(options) {
  var config = {
    search: true,
    height: '15rem',
    placeholder: 'select',
    txtSelected: 'selected',
    txtAll: 'All',
    txtRemove: 'Remove',
    txtSearch: 'search',
    ...options
  };

  function newEl(tag, attrs) {
    var e = document.createElement(tag);
    if (attrs !== undefined) Object.keys(attrs).forEach(k => {
      if (k === 'class') { Array.isArray(attrs[k]) ? attrs[k].forEach(o => o !== '' ? e.classList.add(o) : 0) : (attrs[k] !== '' ? e.classList.add(attrs[k]) : 0) }
      else if (k === 'style') {
        Object.keys(attrs[k]).forEach(ks => {
          e.style[ks] = attrs[k][ks];
        });
      }
      else if (k === 'text') { attrs[k] === '' ? e.innerHTML = '&nbsp;' : e.innerText = attrs[k] }
      else e[k] = attrs[k];
    });
    return e;
  }


  document.querySelectorAll("select[multiple]").forEach((el, k) => {

    var div = newEl('div', { class: 'multiselect-dropdown', style: { width: config.style?.width ?? el.clientWidth + 'px', padding: config.style?.padding ?? '' } });
    el.style.display = 'none';
    el.parentNode.insertBefore(div, el.nextSibling);
    var listWrap = newEl('div', { class: 'multiselect-dropdown-list-wrapper' });
    var list = newEl('div', { class: 'multiselect-dropdown-list', style: { height: config.height } });
    var search = newEl('input', { class: ['multiselect-dropdown-search'].concat([config.searchInput?.class ?? 'form-control']), style: { width: '100%', display: el.attributes['multiselect-search']?.value === 'true' ? 'block' : 'none' }, placeholder: config.txtSearch });
    listWrap.appendChild(search);
    div.appendChild(listWrap);
    listWrap.appendChild(list);

    el.loadOptions = () => {
      list.innerHTML = '';

      if (el.attributes['multiselect-select-all']?.value == 'true') {
        var op = newEl('div', { class: 'multiselect-dropdown-all-selector' })
        var ic = newEl('input', { type: 'checkbox' });
        op.appendChild(ic);
        op.appendChild(newEl('label', { text: config.txtAll }));

        op.addEventListener('click', () => {
          op.classList.toggle('checked');
          op.querySelector("input").checked = !op.querySelector("input").checked;

          var ch = op.querySelector("input").checked;
          list.querySelectorAll(":scope > div:not(.multiselect-dropdown-all-selector)")
            .forEach(i => { if (i.style.display !== 'none') { i.querySelector("input").checked = ch; i.optEl.selected = ch } });

          el.dispatchEvent(new Event('change'));
        });
        ic.addEventListener('click', (ev) => {
          ic.checked = !ic.checked;
        });

        list.appendChild(op);
      }

      Array.from(el.options).map(o => {
        var op = newEl('div', { class: o.selected ? 'checked' : '', optEl: o })
        var ic = newEl('input', { type: 'checkbox', checked: o.selected });
        op.appendChild(ic);
        op.appendChild(newEl('label', { text: o.text }));

        op.addEventListener('click', () => {
          op.classList.toggle('checked');
          op.querySelector("input").checked = !op.querySelector("input").checked;
          op.optEl.selected = !!!op.optEl.selected;
          el.dispatchEvent(new Event('change'));
        });
        ic.addEventListener('click', (ev) => {
          ic.checked = !ic.checked;
        });
        o.listitemEl = op;
        list.appendChild(op);
      });
      div.listEl = listWrap;

      div.refresh = () => {
        div.querySelectorAll('span.optext, span.placeholder').forEach(t => div.removeChild(t));
        var sels = Array.from(el.selectedOptions);
        if (sels.length > (el.attributes['multiselect-max-items']?.value ?? 5)) {
          div.appendChild(newEl('span', { class: ['optext', 'maxselected'], text: sels.length + ' ' + config.txtSelected }));
        }
        else {
          sels.map(x => {
            var c = newEl('span', { class: 'optext', text: x.text, srcOption: x });
            if ((el.attributes['multiselect-hide-x']?.value !== 'true'))
              c.appendChild(newEl('span', { class: 'optdel', text: '🗙', title: config.txtRemove, onclick: (ev) => { c.srcOption.listitemEl.dispatchEvent(new Event('click')); div.refresh(); ev.stopPropagation(); } }));

            div.appendChild(c);
          });
        }
        if (0 == el.selectedOptions.length) div.appendChild(newEl('span', { class: 'placeholder', text: el.attributes['placeholder']?.value ?? config.placeholder }));
      };
      div.refresh();
    }
    el.loadOptions();

    search.addEventListener('input', () => {
      list.querySelectorAll(":scope div:not(.multiselect-dropdown-all-selector)").forEach(d => {
        var txt = d.querySelector("label").innerText.toUpperCase();
        d.style.display = txt.includes(search.value.toUpperCase()) ? 'block' : 'none';
      });
    });

    div.addEventListener('click', () => {
      div.listEl.style.display = 'block';
      search.focus();
      search.select();
    });

    document.addEventListener('click', function(event) {
      if (!div.contains(event.target)) {
        listWrap.style.display = 'none';
        div.refresh();
      }
    });
  });
}

window.addEventListener('load', () => {
  MultiselectDropdown(window.MultiselectDropdownOptions);
});
