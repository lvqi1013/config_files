这是一个用于存放各种配置文件的仓库。


<h1 align="center" style="font-size: 40px;color: #007acc;font-family: 'Courier New', Courier, monospace;">配置文件列表</h1>

# <span align="center" style="font-size: 30px;color: #007acc;font-family: 'Courier New', Courier, monospace;">配置文件列表</span>

- [.gitignore](./.gitignore): 用于存放 Git 忽略的文件列表。
    ```bash
    # curl 下载:Windows or Linux
    curl -O https://raw.githubusercontent.com/lvqi1013/config_files/main/.gitignore
    curl -O https://gitee.com/lvqi1013/config_files/raw/main/.gitignore

    # wget 下载:Linux
    wget https://raw.githubusercontent.com/lvqi1013/config_files/main/.gitignore
    wget https://gitee.com/lvqi1013/config_files/raw/main/.gitignore
    ```

    <div class="code-block">
  <button onclick="copyCode(this)">复制</button>
  <pre><code class="language-bash">curl -O https://raw.githubusercontent.com/lvqi1013/config_files/main/.gitignore</code></pre>
</div>

<script>
function copyCode(button) {
  const code = button.nextElementSibling.querySelector('code').innerText;
  navigator.clipboard.writeText(code).then(() => {
    const originalText = button.innerText;
    button.innerText = '已复制';
    setTimeout(() => button.innerText = originalText, 2000);
  });
}
</script>

