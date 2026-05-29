title: Awards
menu_title: Awards
template: page
menu_order: 401
status: skip

At SaTML 2026, we recognize exceptional contributions to the field through a Best Paper Award and Distinguished Reviewer recognitions. Congratulations to all recipients!

## Best Paper Award

<style>
blockquote {
  background-color: #F8F8F8 !important;
  border-left: 2px solid #DDDDDD !important;
  margin: 0 0 0.3rem 0 !important;
  padding: 0.45rem 1.5rem 0.25rem 1.5rem !important;
}
.paper-button {
  color: teal !important;
  border: 1px solid #AAAAAA !important;
  background-color: transparent !important;
  text-decoration: none !important;
  cursor: pointer;
  padding: 0rem 0.4rem !important;
}
.paper-button:hover {
  background-color: rgba(0, 128, 128, 0.08) !important;
}
.paper-button .icon {
  font-size: 0.7em;
  filter: grayscale(100%);
  margin-right: 4px;
}
section.section .container a.paper-button {
  text-decoration: none !important;
}
.reviewer-grid {
  display: grid;
  grid-template-columns: auto auto auto auto;
  column-gap: 0.5rem;
  row-gap: 0.25rem;
  align-items: baseline;
}
.reviewer-grid div:nth-child(4n+2) {
  padding-right: 1.5rem;
}
@media (max-width: 800px) {
  .reviewer-grid {
    grid-template-columns: auto auto;
  }
  .reviewer-grid div:nth-child(4n+2) {
    padding-right: 0;
  }
}
</style>

<script>
function toggleAbstract(id) {
  var el = document.getElementById('abstract-' + id);
  el.style.display = el.style.display === 'none' ? 'block' : 'none';
}
</script>

Selected by the PC for its outstanding contribution to secure and trustworthy machine learning.

<blockquote>
  <div class="block" style="margin-bottom: 0.2rem">
    <strong>Efficient and Scalable Implementation of Differentially Private Deep Learning without Shortcuts</strong>
  </div>
  <div class="block" style="margin-bottom: 0.2rem; color: #555;">
    Sebastian Rodriguez Beltran, Marlon Tobaben, Joonas Jälkö (University of Helsinki), Niki Loppi (NVIDIA) and Antti Honkela (University of Helsinki)
  </div>
  <div class="block" style="margin-bottom: 0.5rem">
    <button class="tag paper-button" onclick="toggleAbstract('best-paper')"><span class="icon">📃</span>Abstract</button>
    <a class="tag paper-button" href="https://arxiv.org/abs/2406.17298" target="_blank"><span class="icon">📚</span>Arxiv</a>
  </div>
  <div id="abstract-best-paper" style="display: none;">
    <p style="font-size: 0.9em;">Differentially private stochastic gradient descent (DP-SGD) is the standard algorithm for training machine learning models under differential privacy (DP). The most common DP-SGD privacy accountants rely on Poisson subsampling to ensure the theoretical DP guarantees. Implementing computationally efficient DP-SGD with Poisson subsampling is not trivial, which leads to many implementations taking a shortcut by using computationally faster subsampling. We quantify the computational cost of training deep learning models under DP by implementing and benchmarking efficient methods with the correct Poisson subsampling. We find that using the naive implementation of DP-SGD with Opacus in PyTorch has a throughput between 2.6 and 8 times lower than that of SGD. However, efficient gradient clipping implementations like Ghost Clipping can roughly halve this cost. We propose an alternative computationally efficient implementation of DP-SGD with JAX that uses Poisson subsampling and performs comparably with efficient clipping optimizations based on PyTorch. We study the scaling behavior using up to 80 GPUs and find that DP-SGD scales better than SGD.</p>
  </div>
</blockquote>

## Distinguished Reviewers

We are grateful to all our PC members for their dedication and hard work. The following reviewers stood out for their exceptional engagement.

<div class="reviewer-grid">
  <div><strong>Antonio Emanuele Cina</strong></div><div>University of Genoa</div>
  <div><strong>Avital Shafran</strong></div><div>The Hebrew University</div>
  <div><strong>Giovanni Apruzzese</strong></div><div>University of Liechtenstein</div>
  <div><strong>Joel Daniel Andersson</strong></div><div>Institute of Science and Technology Austria</div>
  <div><strong>Rafael Pinot</strong></div><div>Sorbonne University</div>
  <div><strong>Scott Coull</strong></div><div>Google</div>
  <div><strong>Tudor Cebere</strong></div><div>INRIA</div>
  <div><strong>Vera Rimmer</strong></div><div>DistriNet, KU Leuven</div>
</div>
