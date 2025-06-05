title: Program
template: base
menu_order: 200
menu_title: Program
status: skip

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"><script>

#### Overview

The SaTML 2025 conference will be held from April 9–11, 2025, at the University of Copenhagen. The program features keynote talks, paper presentations, a poster session, and a competition track.

- [Day 1 - Wednesday, April 9](#0409)
- [Day 2 - Thursday, April 10](#0410)
- [Day 3 - Friday, April 11](#0411)

For a high-level overview of the conference schedule, please visit our [Google Calendar](https://calendar.google.com/calendar/embed?src=c_ae1443e18cf0a904339e64b26cc4704d039fb9efdfbb5dcac5b96cef2dcc9da7%40group.calendar.google.com&ctz=Europe%2FBerlin&mode=WEEK&dates=20250409%2F20250411). You can also subscribe to the calendar via this [iCal Link](https://calendar.google.com/calendar/ical/c_ae1443e18cf0a904339e64b26cc4704d039fb9efdfbb5dcac5b96cef2dcc9da7%40group.calendar.google.com/public/basic.ics).

#### Location

All events will take place in the [Lundbeckfond Auditorium](https://www.biocenter.ku.dk/english/auditorium/) at the University of Copenhagen, except for the poster session and reception. The poster session and reception will be held in the ground floor lobby of the HC Ørsted Institute, located just a [6-minute walk](https://maps.app.goo.gl/T7TCK8F5FEuSFnqj8) from the auditorium. 

<hr>


<a class='anchor' name='0409'></a>
#### <div class='day-title'>Wednesday, April 9, 2025</div>
<h5 class='opening'> <div class='slot-time'>08:40&ndash;09:00</div> <a class='anchor' name='04090840'></a> <div class='slot-title opening'>Opening Remarks</div>
</h5>
<h5 class='keynote'> <div class='slot-time'>09:00&ndash;09:40</div> <a class='anchor' name='04090900'></a> <div class='slot-title keynote'>Keynote 1</div>
</h5>
<p class='session-chair'>Session Chair: <b>Konrad Rieck</b></p>
<ul class='paper-list program'>
<li class='paper-item program keynote'>
    <em class='paper-title'>Malice, Models and Middlemen</em> <br> 
    Michael Veale (University College London)<br>
    <div class='button-group'>
    <a href="/keynotes/#keynote1" class='button'><small>📃</small> Abstract</a>
    <a href="https://profiles.ucl.ac.uk/53958" class='button'><small>👤</small> Speaker</a>
    </div>
</li> 
</ul>

<h5 class='coffee'> <div class='slot-time'>09:40&ndash;10:00</div> <a class='anchor' name='04090940'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>10:00&ndash;11:00</div> <a class='anchor' name='04091000'></a> <div class='slot-title session'>Session: Security of LLMs</div>
</h5>
<p class='session-chair'>Session Chair: <b>Pavel Laskov</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Non-Halting Queries: Exploiting Fixed Points in LLMs</em> <br> 
    Ghaith&nbsp;Hammouri, Kemal&nbsp;Derya, Berk&nbsp;Sunar (WPI) <br>
    <div class='button-group'>
        <span class='button' id='spot-87'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2410.06287'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-87'>
        We introduce a new vulnerability that exploits fixed points in autoregressive models and use it to craft queries that never halt, i.e. an LLM output that does not terminate. More precisely, for what we call non-halting queries, the LLM never samples the end-of-string token <eos>. We rigorously analyze the conditions under which the non-halting anomaly presents itself. In particular, at temperature zero, we prove that if a repeating (cyclic) sequence of tokens are observed at the output beyond the context size, then the LLM does not halt.   We demonstrate the non-halting in a number of experiments performed in base unaligned models where repeating prompts immediately lead to a non-halting cyclic behavior as predicted by the analysis. Further, we develop a simple recipe that takes the same fixed points observed in the base model and creates a prompt structure %that samples the fixed points from a context to target aligned models. We study the recipe behavior in bypassing alignment in a number of LLMs including gpt-4o, llama-3.1-8b-instruct and gemma-2-9b-it where all models are forced into a non-halting state. Further, we demonstrate the success of the recipe in sending every major model released over the past year into a non-halting state with the same simple prompt even over higher temperatures. We also study direct inversion based techniques to craft new short prompts to induce the non-halting state. Our experiments with the gradient search based inversion technique ARCA show that non-halting is prevalent across models and may be easily induced with a few input tokens.  While its impact on the reliability of hosted systems can be mitigated by configuring a hard maximum token limit in the sampler, the non-halting anomaly still manages to break alignment. This underlies the need for further studies and stronger forms of alignment against non-halting anomalies. 
    </blockquote>
    <script>
        $("#spot-87").click(function(){
            $("#abstract-87").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Jailbreaking Black Box Large Language Models in Twenty Queries</em> <br> 
    Patrick&nbsp;Chao, Alexander&nbsp;Robey, Edgar&nbsp;Dobriban, Hamed&nbsp;Hassani, George J.&nbsp;Pappas, Eric&nbsp;Wong (University&nbsp;of&nbsp;Pennsylvania) <br>
    <div class='button-group'>
        <span class='button' id='spot-95'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-95'>
        There is growing interest in ensuring that large language models (LLMs) align with human values. However, the alignment of such models is vulnerable to adversarial jailbreaks, which coax LLMs into overriding their safety guardrails. The identification of these vulnerabilities is therefore instrumental in understanding inherent weaknesses and preventing future misuse.  To this end, we propose <em>Prompt Automatic Iterative Refinement</em> (PAIR), an algorithm that generates semantic jailbreaks with only black-box access to an LLM. PAIR&mdash;which is inspired by social engineering attacks&mdash;uses an attacker LLM to automatically generate jailbreaks for a separate targeted LLM without human intervention. In this way, the attacker LLM iteratively queries the target LLM to update and refine a candidate jailbreak. Empirically, PAIR often requires fewer than twenty queries to produce a jailbreak, which is orders of magnitude more efficient than existing algorithms.  PAIR also achieves competitive jailbreaking success rates and transferability on open and closed-source LLMs, including GPT-3.5/4, Vicuna, and Gemini. 
    </blockquote>
    <script>
        $("#spot-95").click(function(){
            $("#abstract-95").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Get my drift? Catching LLM Task Drift with Activation Deltas</em> <br> 
    Sahar&nbsp;Abdelnabi, Aideen&nbsp;Fay, Giovanni&nbsp;Cherubin, Ahmed&nbsp;Salem (Microsoft), Mario&nbsp;Fritz (CISPA&nbsp;Helmholtz&nbsp;Center&nbsp;for&nbsp;Information&nbsp;Security), Andrew&nbsp;Paverd (Microsoft) <br>
    <div class='button-group'>
        <span class='button' id='spot-137'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2406.00799'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-137'>
        Large Language Models (LLMs) are commonly used in retrieval-augmented applications to execute user instructions based on data from external sources. For example, modern search engines use LLMs to answer queries based on relevant search results; email plugins summarize emails by processing their content through an LLM. However, the potentially untrusted provenance of these data sources can lead to prompt injection attacks, where the LLM is manipulated by natural language instructions embedded in the external data, causing it to deviate from the user’s original instruction(s). We define this deviation as task drift. Task drift is a significant concern as it allows attackers to exfiltrate data or influence the LLM’s output for other users. We study LLM activations as a solution to detect task drift, showing that activation deltas - the difference in activations before and after processing external data - are strongly correlated with this phenomenon. Through two probing methods, we demonstrate that a simple linear classifier can detect drift with near-perfect ROC AUC on an out-of-distribution test set. We evaluate these methods by making minimal assumptions about how user’s tasks, system prompts, and attacks can be phrased. We observe that this approach generalizes surprisingly well to unseen task domains, such as prompt injections, jailbreaks, and malicious instructions, without being trained on any of these attacks. Interestingly, the fact that this solution does not require any modifications to the LLM (e.g., fine-tuning), as well as its compatibility with existing meta-prompting solutions, makes it cost-efficient and easy to deploy. To encourage further research on activation-based task inspection, decoding, and interpretability, we release our large-scale TaskTracker toolkit, featuring a dataset of over 500K instances, representations from six SoTA language models, and a suite of inspection tools. 
    </blockquote>
    <script>
        $("#spot-137").click(function(){
            $("#abstract-137").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Mark My Words: Analyzing and Evaluating Language Model Watermarks</em> <br> 
    Julien&nbsp;Piet, Chawin&nbsp;Sitawarin, Vivian&nbsp;Fang, Norman&nbsp;Mu, David&nbsp;Wagner (UC&nbsp;Berkeley) <br>
    <div class='button-group'>
        <span class='button' id='spot-150'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-150'>
        The capabilities of large language models have grown significantly in recent years and so too have concerns about their misuse. It is important to be able to distinguish machine-generated text from human-authored content. Prior works have proposed numerous schemes to watermark text, which would benefit from a systematic evaluation framework. This work focuses on LLM output watermarking techniques—as opposed to image or model watermarks—and proposes Mark My Words, a comprehensive benchmark for them under different natural language tasks.   We focus on three main metrics: quality, size (i.e., the number of tokens needed to detect a watermark), and tamper resistance (i.e., the ability to detect a watermark after perturbing marked text). Current watermarking techniques are nearly practical enough for real-world use: Kirchenbauer et al. [33]’s scheme can watermark models like Llama 2 7B-chat or Mistral-7B-Instruct with no perceivable loss in quality on natural language tasks, the watermark can be detected with fewer than 100 tokens, and their scheme offers good tamper resistance to simple perturbations. However, they struggle to efficiently watermark code generations.   We publicly release our benchmark (https://anonymous.4open.science/r/MarkMyWords). 
    </blockquote>
    <script>
        $("#spot-150").click(function(){
            $("#abstract-150").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>11:00&ndash;11:20</div> <a class='anchor' name='04091100'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>11:20&ndash;12:20</div> <a class='anchor' name='04091120'></a> <div class='slot-title session'>Session: Adversaries and Attacks</div>
</h5>
<p class='session-chair'>Session Chair: <b>Lea Schönherr</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>SnatchML: Hijacking ML models without Training Access</em> <br> 
    Mahmoud&nbsp;Ghorbal (Université&nbsp;Polytechnique&nbsp;Hauts-de-France), Halima&nbsp;Bouzidi (CSIT,&nbsp;Queen's&nbsp;University&nbsp;Belfast), Ioan Marius&nbsp;Bilasco (Université&nbsp;de&nbsp;Lille), Ihsen&nbsp;Alouani (CSIT,&nbsp;Queen's&nbsp;University&nbsp;Belfast) <br>
    <div class='button-group'>
        <span class='button' id='spot-72'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-72'>
        The widespread deployment of Machine Learning (ML) models has been accompanied by the emergence of various attacks that threaten their trustworthiness and raise ethical and societal concerns. One such attack is model hijacking, where an adversary seeks to repurpose a victim model to perform a different task than originally intended. Model hijacking can cause significant accountability and security risks since the owner of a hijacked model can be framed for having their model offer illegal or unethical services.  Prior works consider model hijacking as a training time attack, whereby an adversary requires full access to the ML model training.  In this paper, we consider a stronger threat model for an inference-time hijacking attack, where the adversary has no access to the training phase of the victim model.  Our intuition is that ML models, which are typically over-parameterized, might have the capacity to (unintentionally) learn more than the intended task they are trained for.  We propose SnatchML, a new training-free model hijacking attack, that leverages the extra capacity learnt by the victim model to infer different tasks that can be semantically related or unrelated to the original one.  Our results on models deployed on AWS Sagemaker showed that SnatchML can deliver high accuracy on hijacking tasks. Interestingly, while all previous approaches are limited by the number of classes in the benign task, SnatchML can hijack models for tasks that contain more classes than the original. We explore different methods to mitigate this risk; We propose meta-unlearning, which is designed to help the model unlearn a potentially malicious task while training for the original task. We also provide insights on <em>over-parametrization</em> as a possible inherent factor that facilitates model hijacking, and accordingly, we propose a compression-based countermeasure to counteract this attack. We believe this work offers a previously overlooked perspective on model hijacking attacks, presenting a stronger threat model and higher applicability in real-world contexts. 
    </blockquote>
    <script>
        $("#spot-72").click(function(){
            $("#abstract-72").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>TS-Inverse: A Gradient Inversion Attack tailored for Federated Time Series Forecasting Models</em> <br> 
    Caspar&nbsp;Meijer, Jiyue&nbsp;Huang (TU&nbsp;Delft), Shreshtha&nbsp;Sharma, Elena&nbsp;Lazovik (TNO), Lydia Y.&nbsp;Chen (TU&nbsp;Delft) <br>
    <div class='button-group'>
        <span class='button' id='spot-127'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2503.20952'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-127'>
        Federated learning (FL) for time series forecasting (TSF) enables clients with privacy-sensitive time series (TS) data to collaboratively learn accurate forecasting models, e.g., in energy load prediction. Unfortunately, privacy risks in FL persist, as servers can potentially reconstruct clients’ training data through gradient inversion attacks (GIA). While GIA is demonstrated for image classification tasks, little is known for time series regression tasks. In this paper, we first conduct an extensive empirical study on inverting TS data across 4 TSF models and 4 datasets, identifying the unique challenges of reconstructing both observations and targets of TS data. We then propose TS-Inverse, a novel GIA that improves the inversion of TS data through (i) learning a gradient inversion model that outputs quantile predictions, (ii) a unique loss function incorporating periodicity and trend regularization, and (iii) regularization according to the quantile predictions. Our evaluations demonstrate a remarkable performance of TSInverse, achieving at least 2x-10x improvement in terms of sMAPE metric over existing GIA methods on TS data. Code repository: www.github.com/⟨anonymous⟩/⟨anonymous⟩ 
    </blockquote>
    <script>
        $("#spot-127").click(function(){
            $("#abstract-127").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>PEEL the Layers and Find Yourself: Revisiting Inference-time Data Leakage for Residual Neural Networks</em> <br> 
    Huzaifa&nbsp;Arif (Rensselaer&nbsp;Polytechnic&nbsp;Institute), Pin-Yu&nbsp;Chen, Keerthiram&nbsp;Murugesan, Payel&nbsp;Das (IBM), Alex&nbsp;Gittens (RPI) <br>
    <div class='button-group'>
        <span class='button' id='spot-176'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-176'>
        This paper explores inference-time data leakage risks of deep neural networks (NNs), where a curious and honest model service provider is interested in retrieving users' private data inputs solely based on the model inference results. Particularly, we revisit residual NNs due to their popularity in computer vision and our hypothesis that residual blocks are a primary cause of data leakage owing to the use of skip connections. By formulating inference-time data leakage as a constrained optimization problem, we propose a novel backward feature inversion method, <strong>PEEL</strong>, which can effectively recover block-wise input features from the intermediate output of residual NNs. The surprising results in high-quality input data recovery can be explained by the intuition that the output from these residual blocks can be considered as a noisy version of the input and thus the output retains sufficient information for input recovery. We demonstrate the effectiveness of our layer-by-layer feature inversion method on facial image datasets and pre-trained classifiers. Our results show that PEEL outperforms the state-of-the-art recovery methods by an order of magnitude when evaluated by mean squared error (MSE). 
    </blockquote>
    <script>
        $("#spot-176").click(function(){
            $("#abstract-176").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Attackers Can Do Better: Over- and Understated Factors of Model Stealing Attacks</em> <br> 
    Daryna&nbsp;Oliynyk, Rudolf&nbsp;Mayer (SBA&nbsp;Research), Andreas&nbsp;Rauber (TU&nbsp;Wien) <br>
    <div class='button-group'>
        <span class='button' id='spot-192'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2503.06188'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-192'>
        Machine learning (ML) models were shown to be vulnerable to different security attacks &ndash; including model stealing attacks, which lead to intellectual property infringement. Among other attack types, substitute model training is an all-encompassing attack applicable to any machine learning model whose behaviour can be approximated from input-output queries. Whereas previous works mainly focused on improving the performance of substitute models by, e.g. developing a new substitute training method, there have been only limited comprehensive ablation studies that try to understand the impact the strength of an attacker has on the substitute model's performance. As a result, different authors came to diverse, sometimes contradicting conclusions. In this work, we therefore exhaustively examine the influence of different factors, primarily forming the attacker's capabilities and knowledge, on a substitute training attack. We investigate how the quality of the substitute training data, the training strategy, and discrepancies between the characteristics of the target and substitute models impact the performance of the attack.  Our findings suggest that some of the factors that have been considered important in the past are, in fact, not that influential; instead, we discover new correlations between the attack conditions and success rate. Moreover, our results often exceed or match the performance of attacks that assume a stronger attacker, suggesting that these stronger attacks are likely endangering a model owner's intellectual property to a significantly higher degree than shown until now. 
    </blockquote>
    <script>
        $("#spot-192").click(function(){
            $("#abstract-192").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='lunch'> <div class='slot-time'>12:20&ndash;13:30</div> <a class='anchor' name='04091220'></a> <div class='slot-title lunch'>Lunch Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>13:30&ndash;14:30</div> <a class='anchor' name='04091330'></a> <div class='slot-title session'>Session: Backdoor Attacks</div>
</h5>
<p class='session-chair'>Session Chair: <b>Yigitcan Kaya</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Backdoor Detection through Replicated Execution of Outsourced Training</em> <br> 
    Hengrui&nbsp;Jia, Sierra&nbsp;Wyllie (University&nbsp;of&nbsp;Toronto&nbsp;and&nbsp;Vector&nbsp;Institute), Akram Bin&nbsp;Sediq, Ahmed A.&nbsp;Ibrahim (Ericsson&nbsp;Canada), Nicolas&nbsp;Papernot (University&nbsp;of&nbsp;Toronto&nbsp;and&nbsp;Vector&nbsp;Institute) <br>
    <div class='button-group'>
        <span class='button' id='spot-10'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2504.00170'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-10'>
        It is common practice to outsource the training of machine learning models to cloud providers. Clients who do so gain from the cloud's economies of scale, but implicitly assume trust: the server should not deviate from the client's training procedure. A malicious server may, for instance, seek to insert backdoors in the model. Detecting a backdoored model without prior knowledge of both the backdoor attack and its accompanying trigger remains a challenging problem. In this paper, we show that a client with access to multiple cloud providers can replicate a subset of training steps across multiple servers to detect deviation from the training procedure in a similar manner to differential testing. Assuming some cloud-provided servers are benign, we identify malicious servers by the substantial difference between model updates required for backdooring and those resulting from clean training. Perhaps the strongest advantage of our approach is its suitability to clients that have limited-to-no local compute capability to perform training; we leverage the existence of multiple cloud providers to identify malicious updates without expensive human labeling or heavy computation. We demonstrate the capabilities of our approach on an outsourced supervised learning task where <em>50%</em> of the cloud providers insert their own backdoor; our approach is able to correctly identify <em>99.6%</em> of them. In essence, our approach is successful because it replaces the signature-based paradigm taken by existing approaches with an anomaly-based detection paradigm. Furthermore, our approach is robust to several attacks from adaptive adversaries utilizing knowledge of our detection scheme. 
    </blockquote>
    <script>
        $("#spot-10").click(function(){
            $("#abstract-10").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Robust Knowledge Distillation in Federated Learning: Counteracting Backdoor Attacks</em> <br> 
    Ebtisaam&nbsp;Alharbi (Lancaster&nbsp;University;&nbsp;Umm&nbsp;AlQura&nbsp;University), Leandro Soriano&nbsp;Marcolino, Qiang&nbsp;Ni, Antonios&nbsp;Gouglidis (Lancaster&nbsp;University) <br>
    <div class='button-group'>
        <span class='button' id='spot-50'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2502.00587'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-50'>
        Federated Learning (FL) enables collaborative model training across multiple devices while preserving data privacy. However, it remains susceptible to backdoor attacks, where malicious participants can compromise the global model. Existing defence methods are limited by strict assumptions on data heterogeneity (Non-Independent and Identically Distributed data) and the proportion of malicious clients, reducing their practicality and effectiveness. To overcome these limitations, we propose Robust Knowledge Distillation (RKD), a novel defence mechanism that enhances model integrity without relying on restrictive assumptions. RKD integrates clustering and model selection techniques to identify and filter out malicious updates, forming a reliable ensemble of models. It then employs knowledge distillation to transfer the collective insights from this ensemble to a global model. Extensive evaluations demonstrate that RKD effectively mitigates backdoor threats while maintaining high model performance, outperforming current state-of-the-art defence methods across various scenarios. 
    </blockquote>
    <script>
        $("#spot-50").click(function(){
            $("#abstract-50").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>The Ultimate Cookbook for Invisible Poison: Crafting Subtle Clean-Label Text Backdoors with Style Attributes</em> <br> 
    Wencong&nbsp;You, Daniel&nbsp;Lowd (University&nbsp;of&nbsp;Oregon) <br>
    <div class='button-group'>
        <span class='button' id='spot-194'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-194'>
        Backdoor attacks on text classifiers can cause them to predict a predefined label when a particular "trigger" is present. However, the triggers used are often ungrammatical or otherwise conspicuous. As a result, human annotators, who play a critical role in curating training data, can easily detect and filter out these unnatural texts during manual inspection, reducing the risk of such attacks. We argue that a key criterion for a successful attack is for text with and without triggers to be indistinguishable to humans. To that end, we propose a new backdoor attack, Attribute Backdoor (AttrBkd), which uses fine-grained style attributes as triggers. The triggers are added by an instruct-tuned LLM, which paraphrases the input text using the specified attribute. We propose three recipes for crafting effective trigger attributes, such as extracting the attributes from existing baseline backdoor attacks. Our comprehensive human and automated evaluations find that AttrBkd with these baseline-derived attributes is often more effective (higher attack success rate) and more subtle (fewer instances detected by humans) than the original baseline backdoor attacks. Our human annotation also provides information not captured by automated metrics used in prior work, and scrutinizes the misalignment of these metrics with human judgment. 
    </blockquote>
    <script>
        $("#spot-194").click(function(){
            $("#abstract-194").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Krait: A Backdoor Attack Against Graph Prompt Tuning</em> <br> 
    Ying&nbsp;Song (University&nbsp;of&nbsp;Pittsburgh), Rita&nbsp;Singh (Carnegie&nbsp;Mellon&nbsp;University), Balaji&nbsp;Palanisamy (University&nbsp;of&nbsp;Pittsburgh) <br>
    <div class='button-group'>
        <span class='button' id='spot-153'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2407.13068'><small>📚</small> Arxiv</a> <span class='button no-border no-link'>⚠️ Video talk</span>
    </div>
    <blockquote class='paper-abstract' id='abstract-153'>
        Graph prompt tuning has emerged as a promising paradigm to effectively transfer general graph knowledge from pre-trained models to various downstream tasks, particularly in few-shot contexts. However, its susceptibility to backdoor attacks, where adversaries insert triggers to manipulate outcomes, raises a critical concern. We conduct the first study to investigate such vulnerability, revealing that backdoors can disguise benign graph prompts, thus evading detection. We introduce Krait, a novel graph prompt backdoor. Specifically, we propose a simple yet effective model-agnostic metric called label non-uniformity homophily to select poisoned candidates, significantly reducing computational complexity. To accommodate diverse attack scenarios and advanced attack types, we design three customizable trigger generation methods to craft prompts as triggers. We propose a novel centroid similarity-based loss function to optimize prompt tuning for attack effectiveness and stealthiness. Experiments on four real-world graphs demonstrate that Krait can efficiently embed triggers to merely 0.15% to 2% of training nodes, achieving high attack success rates without sacrificing clean accuracy. Notably, in one-to-one and all-to-one attacks, Krait can achieve 100% attack success rates by poisoning as few as 2 and 22 nodes, respectively. Our experiments further show that Krait remains potent across different transfer cases, attack types, and graph neural network backbones. Additionally, Krait can be successfully extended to the black-box setting, posing more severe threats. Finally, we analyze why Krait can evade both classical and state-of-the-art defenses, and provide practical insights for detecting and mitigating this class of attacks. 
    </blockquote>
    <script>
        $("#spot-153").click(function(){
            $("#abstract-153").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='coffee'> <div class='slot-time'>14:30&ndash;14:50</div> <a class='anchor' name='04091430'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='competitions'> <div class='slot-time'>14:50&ndash;15:20</div> <a class='anchor' name='04091450'></a> <div class='slot-title competitions'>Competitions</div>
</h5>
<p class='session-chair'>Session Chair: <b>Konrad Rieck</b></p>
<ul class='paper-list program'>
<li class='paper-item program competition'>
    <em class='paper-title'>🏁 Adaptive Prompt Injection: LLMail Inject</em> <br>
    <div class='button-group'>
    <a class='button' href="/competitions/#competition1"><small>📃</small> Abstract</a>
    <a class='button' href="https://microsoft.github.io/llmail-inject/"><small>🌐</small> Website</a>
    </div>
</li><li class='paper-item program competition'>
    <em class='paper-title'>🏁 Membership Inference on Diffusion-model-based Synthetic Tabular Data</em> <br>
    <div class='button-group'>
    <a class='button' href="/competitions/#competition3"><small>📃</small> Abstract</a>
    <a class='button' href="https://vectorinstitute.github.io/MIDST"><small>🌐</small> Website</a>
    </div>
</li></ul>

<h5 class='break'> <div class='slot-time'>15:20&ndash;15:40</div> <a class='anchor' name='04091520'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>15:40&ndash;16:40</div> <a class='anchor' name='04091540'></a> <div class='slot-title session'>Session: Broader Perspectives</div>
</h5>
<p class='session-chair'>Session Chair: <b>Lorenzo Cavallaro</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>SoK: On the Offensive Potential of AI</em> <br> 
    Saskia Laura&nbsp;Schröer, Giovanni&nbsp;Apruzzese (University&nbsp;of&nbsp;Liechtenstein), Soheil&nbsp;Human (Vienna&nbsp;University&nbsp;of&nbsp;Economics&nbsp;and&nbsp;Business), Pavel&nbsp;Laskov (University&nbsp;of&nbsp;Liechtenstein), Hyrum S.&nbsp;Anderson (Robust&nbsp;Intelligence), Edward W.N.&nbsp;Bernroider (Vienna&nbsp;University&nbsp;of&nbsp;Economics&nbsp;and&nbsp;Business), Aurore&nbsp;Fass (CISPA&nbsp;Helmholtz&nbsp;Center&nbsp;for&nbsp;Information&nbsp;Security), Ben&nbsp;Nassi (Technion&nbsp;-&nbsp;Israel&nbsp;Institute&nbsp;of&nbsp;Technology)), Vera&nbsp;Rimmer (DistriNet,&nbsp;KU&nbsp;Leuven), Fabio&nbsp;Roli (Università&nbsp;degli&nbsp;Studi&nbsp;di&nbsp;Genova), Samer&nbsp;Salam, Chi En (Ashley)&nbsp;Shen (Cisco&nbsp;Systems), Ali&nbsp;Sunyaev (Karlsruhe&nbsp;Institute&nbsp;of&nbsp;Technolog), Tim&nbsp;Wadhwa-Brown (Cisco&nbsp;Systems), Isabel&nbsp;Wagner (University&nbsp;of&nbsp;Basel), Gang&nbsp;Wang (University&nbsp;of&nbsp;Illinois&nbsp;Urbana-Champaign) <br>
    <div class='button-group'>
        <span class='button' id='spot-58'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2412.18442'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-58'>
        Our society increasingly benefits from Artificial Intelligence (AI). Unfortunately, more and more evidence appears that AI is also used for offensive purposes. Prior works have revealed various examples of use cases in which the deployment of AI can lead to violation of security and privacy objectives. No extant work, however, has been able to draw a holistic picture of the offensive potential of AI. In this SoK paper we seek to lay the ground for a systematic analysis of the heterogeneous capabilities of offensive AI. In particular we (i) account for AI risks to both humans and systems while (ii) consolidating and distilling knowledge from academic literature, expert opinions, industrial venues, as well as laymen—all of which being valuable sources of information on offensive AI.  To enable alignment of such diverse sources of knowledge, we devise a common set of criteria reflecting essential technological factors related to offensive AI. With the help of such criteria, we systematically analyze: 95 research papers; 38 InfoSec briefings (from, e.g., BlackHat); the thoughts of 549 participants of a survey we carried out with the general population; and the opinion of 12 experts. Our contributions not only reveal concerning ways (some of which overlooked by prior work) in which AI can be offensively used today, but also represent a foothold to address this threat in the years to come. 
    </blockquote>
    <script>
        $("#spot-58").click(function(){
            $("#abstract-58").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Contextual Confidence and Generative AI</em> <br> 
    Shrey&nbsp;Jain (Microsoft), Zoe&nbsp;Hitzig (Harvard/OpenAI), Pamela&nbsp;Mishkin (OpenAI) <br>
    <div class='button-group'>
        <span class='button' id='spot-96'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-96'>
        Generative AI models perturb the foundations of effective human communication. They present new challenges to what we call contextual confidence, disrupting participants’ ability to identify the authentic context of communication and their ability to protect communication from reuse and recombination outside its intended context. In this paper, we describe strategies – tools, technologies and policies – that aim to stabilize communication in the face of these challenges. The strategies we discuss fall into two broad categories. Containment strategies aim to reassert context in environments where it is currently threatened – a reaction to the context-free expectations and norms established by the internet. Mobilization strategies, by contrast, view the rise of generative AI as an opportunity to proactively set new and higher expectations around privacy and authenticity in mediated communication. We apply this framework to a hypothetical scenario to show its value in pointing toward solutions to privacy and authenticity concerns in emerging uses of generative AI. 
    </blockquote>
    <script>
        $("#spot-96").click(function(){
            $("#abstract-96").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Locking Machine Learning Models into Hardware</em> <br> 
    Eleanor&nbsp;Clifford (Imperial&nbsp;College&nbsp;London), Adhithya&nbsp;Saravanan, Harry&nbsp;Langford (University&nbsp;of&nbsp;Cambridge), Cheng&nbsp;Zhang, Yiren&nbsp;Zhao (Imperial&nbsp;College&nbsp;London), Robert&nbsp;Mullins (University&nbsp;of&nbsp;Cambridge), Ilia&nbsp;Shumailov, Jamie&nbsp;Hayes (Google&nbsp;Deepmind) <br>
    <div class='button-group'>
        <span class='button' id='spot-141'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2405.20990'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-141'>
        Modern Machine Learning models are expensive IP and business competitiveness often depends on keeping this IP confidential. This in turn restricts how these models are deployed &ndash; for example it is unclear how to deploy a model on-device without inevitably leaking the underlying model. At the same time, confidential computing technologies such as Multi-Party Computation or Homomorphic encryption remain impractical for wide adoption. In this paper we take a different approach and investigate feasibility of ML-specific mechanisms that deter unauthorized model use by restricting the model to only be usable on specific hardware, making adoption on unauthorized hardware inconvenient. That way, even if IP is compromised, it cannot be trivially used without specialised hardware or major model adjustment. In a sense, we seek to enable cheap <em>locking of machine learning models into specific hardware</em>. We demonstrate that <em>locking</em> mechanisms are feasible by either targeting efficiency of model representations, making such models incompatible with quantisation, or tying the model's operation to specific characteristics of hardware, such as the number of clock cycles for arithmetic operations. We demonstrate that locking comes with negligible work and latency overheads, while significantly restricting usability of the resultant model on unauthorized hardware. 
    </blockquote>
    <script>
        $("#spot-141").click(function(){
            $("#abstract-141").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Position: Episodic memory in AI agents poses risks that should be studied and mitigated</em> <br> 
    Chad&nbsp;DeChant (Columbia&nbsp;University) <br>
    <div class='button-group'>
        <span class='button' id='spot-178'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2501.11739'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-178'>
        Most current AI models have little ability to store and later retrieve a record or representation of what they do. In human cognition, episodic memories play an important role in both recall of the past as well as planning for the future. The ability to form and use episodic memories would similarly enable a broad range of improved capabilities in an AI agent that interacts with and takes actions in the world. Researchers have begun directing more attention to developing memory abilities in AI models. It is therefore likely that models with such capability will be become widespread in the near future. This could in some ways contribute to making such AI agents safer by enabling users to better monitor, understand, and control their actions. However, as a new capability with wide applications, we argue that it will also introduce significant new risks that researchers should begin to study and address. We outline these risks and benefits and propose four principles to guide the development of episodic memory capabilities so that these will enhance, rather than undermine, the effort to keep AI safe and trustworthy. 
    </blockquote>
    <script>
        $("#spot-178").click(function(){
            $("#abstract-178").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>16:40&ndash;17:00</div> <a class='anchor' name='04091640'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='posters'> <div class='slot-time'>17:00&ndash;20:00</div> <a class='anchor' name='04091700'></a> <div class='slot-title posters'>Poster Session and Reception</div>
</h5>
<ul class='paper-list program'>
<li class='paper-item program poster'><b>Note:</b> The poster session and reception will be held at HC. Ørsted Institute, ground floor lobby. It is located just a <a href='https://maps.app.goo.gl/T7TCK8F5FEuSFnqj8'>6-minute walk</a> from the Lundbeck Auditorium. The address is <a href='https://maps.app.goo.gl/byv7nKUB1xSqnRB57'>Universitetsparken 5, 2100 Copenhagen.
</li>
</ul>

<br/><hr>

<a class='anchor' name='0410'></a>
#### <div class='day-title'>Thursday, April 10, 2025</div>
<h5 class='keynote'> <div class='slot-time'>09:00&ndash;09:40</div> <a class='anchor' name='04100900'></a> <div class='slot-title keynote'>Keynote 2</div>
</h5>
<p class='session-chair'>Session Chair: <b>Kathrin Grosse</b></p>
<ul class='paper-list program'>
<li class='paper-item program keynote'>
    <em class='paper-title'>The Science of Empirical Privacy Measurement: Memorization and Beyond</em> <br> 
    Kamalika Chaudhuri (University of California San Diego)<br>
    <div class='button-group'>
    <a href="/keynotes/#keynote2" class='button'><small>📃</small> Abstract</a>
    <a href="https://cseweb.ucsd.edu/~kamalika/" class='button'><small>👤</small> Speaker</a>
    </div>
</li> 
</ul>

<h5 class='coffee'> <div class='slot-time'>09:40&ndash;10:00</div> <a class='anchor' name='04100940'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>10:00&ndash;11:00</div> <a class='anchor' name='04101000'></a> <div class='slot-title session'>Session: Membership Inference Attacks</div>
</h5>
<p class='session-chair'>Session Chair: <b>Vera Rimmer</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Position: Membership Inference Attacks Cannot Prove that a Model Was Trained On Your Data</em> <br> 
    Jie&nbsp;Zhang, Debeshee&nbsp;Das (ETH&nbsp;Zurich), Gautam&nbsp;Kamath (University&nbsp;of&nbsp;Waterloo), Florian&nbsp;Tramèr (ETH&nbsp;Zurich) <br>
    <div class='button-group'>
        <span class='button' id='spot-109'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2409.19798'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-109'>
        We consider the problem of a <em>training data proof</em>, where a data creator or owner wants to demonstrate to a third party that some machine learning model was trained on their data. Training data proofs play a key role in recent lawsuits against foundation models trained on web-scale data. Many prior works suggest to instantiate training data proofs using <em>membership inference attacks</em>. We argue that this approach is fundamentally unsound: to provide convincing evidence, the data creator needs to demonstrate that their attack has a low false positive rate, i.e., that the attack's output is unlikely under the <em>null hypothesis</em> that the model was <em>not</em> trained on the target data. Yet, sampling from this null hypothesis is impossible, as we do not know the exact contents of the training set, nor can we (efficiently) retrain a large foundation model. We conclude by offering two paths forward, by showing that data extraction attacks and membership inference on special canary data can be used to create sound training data proofs. 
    </blockquote>
    <script>
        $("#spot-109").click(function(){
            $("#abstract-109").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Range Membership Inference Attacks</em> <br> 
    Jiashu&nbsp;Tao, Reza&nbsp;Shokri (National&nbsp;University&nbsp;of&nbsp;Singapore) <br>
    <div class='button-group'>
        <span class='button' id='spot-129'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2408.05131'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-129'>
        Machine learning models can leak private information about their training data, but the standard methods to measure this risk, based on membership inference attacks (MIAs), have a major limitation. They only check if a given data point <em>exactly</em> matches a training point, neglecting the potential of similar or partially overlapping data revealing the same private information. To address this issue, we introduce the class of range membership inference attacks (RaMIAs), testing if the model was trained on any data in a specified range (defined based on the semantics of privacy). We formulate the RaMIAs game and design a principled statistical test for its composite hypotheses. We show that RaMIAs can capture privacy loss more accurately and comprehensively than MIAs on various types of data, such as tabular, image, and language. RaMIA paves the way for a more comprehensive and meaningful privacy auditing of machine learning algorithms. 
    </blockquote>
    <script>
        $("#spot-129").click(function(){
            $("#abstract-129").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Hyperparameters in Score-Based Membership Inference Attacks</em> <br> 
    Gauri&nbsp;Pradhan, Joonas&nbsp;Jälkö, Marlon&nbsp;Tobaben, Antti&nbsp;Honkela (University&nbsp;of&nbsp;Helsinki) <br>
    <div class='button-group'>
        <span class='button' id='spot-154'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2502.06374'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-154'>
        Membership Inference Attacks (MIAs) have emerged as a valuable framework for evaluating privacy leakage by machine learning models. Score-based MIAs are distinguished, in particular, by their ability to exploit the confidence scores that the model generates for particular inputs. Existing score-based MIAs implicitly assume that the adversary has access to the target model’s hyperparameters, which can be used to train the shadow models for the attack. In this work, we demonstrate that the knowledge of target hyperparameters is not a prerequisite for MIA in the transfer learning setting. Based on this, we propose a novel approach to select the hyperparameters for training the shadow models for MIA when the attacker has no prior knowledge about them by matching the output distributions of target and shadow models. We demonstrate that using the new approach yields hyperparameters that lead to an attack near indistinguishable in performance from an attack that uses target hyperparameters to train the shadow models. Furthermore, we study the empirical privacy risk of unaccounted use of training data for hyperparameter optimization (HPO) in differentially private (DP) transfer learning. We find no statistically significant evidence that performing HPO using training data would increase vulnerability to MIA. 
    </blockquote>
    <script>
        $("#spot-154").click(function(){
            $("#abstract-154").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>SoK: Membership Inference Attacks on LLMs are Rushing Nowhere (and How to Fix It)</em> <br> 
    Matthieu&nbsp;Meeus, Igor&nbsp;Shilov (Imperial&nbsp;College&nbsp;London), Shubham&nbsp;Jain (Sense&nbsp;Street), Manuel&nbsp;Faysse (MICS,&nbsp;CentraleSupélec,&nbsp;Université&nbsp;Paris-Saclay), Marek&nbsp;Rei, Yves-Alexandre&nbsp;de Montjoye (Imperial&nbsp;College&nbsp;London) <br>
    <div class='button-group'>
        <span class='button' id='spot-159'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-159'>
        Whether Large Language models (LLMs) memorize their training data and what this means, from the privacy leakage of finetuning data to detecting copyright violations &mdash; has become a rapidly growing area of research over the last two years. In the last few months, more than <em>10</em> new methods have been proposed to perform sequence-level Membership Inference Attacks (MIAs) against LLMs. Contrary to traditional MIAs which rely on fixed, but randomized records or models, these methods are mostly trained and tested on datasets collected post-hoc. Sets of members and non-members, used to evaluate the MIA, are constructed using informed guesses after the release of a model. This lack of randomization, however, raises concerns of a distribution shift between members and non-members. We here extensively review the literature on MIAs against LLMs and show that, while most work focuses on sequence-level MIAs evaluated in post-hoc setups, the literature considers a range of target models, motivations and units of interest. We then quantify distribution shifts present in the <em>6</em> datasets used in the literature, ranging from books to papers using a model-less bag of word classifier and compare them to MIA results. Our analysis show all of them suffer from such strong distribution shifts that they invalidate the claims of LLMs memorizing strongly in the wild and, potentially, the methodological contributions of the recent papers based on these datasets.   Yet, all hope might not be lost. We introduce important considerations to properly evaluate MIAs against LLMs and discuss, in turn, potential ways forwards: randomized test splits, injections of randomized (unique) sequences, randomized fine-tuning, and several post-hoc control methods. While each option comes with its advantages and limitations, we believe they collectively provide solid grounds to guide the development of MIA methods and study LLM memorization. We conclude by proposing and releasing two comprehensive, easy-to-use benchmarks for sequence-level and document-level MIAs against LLMs. LLM memorization is an extremely important and multi-faceted question, yet meaningful progress can only be achieved with the use of robust, independent benchmarks such as the ones we propose here. 
    </blockquote>
    <script>
        $("#spot-159").click(function(){
            $("#abstract-159").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>11:00&ndash;11:20</div> <a class='anchor' name='04101100'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>11:20&ndash;12:20</div> <a class='anchor' name='04101120'></a> <div class='slot-title session'>Session: Detection and Forensics</div>
</h5>
<p class='session-chair'>Session Chair: <b>Giovanni Apruzzese</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>HALO: Robust Out-of-Distribution Detection via Joint Optimisation</em> <br> 
    Hugo&nbsp;Lyons Keenan, Sarah&nbsp;Erfani, Christopher&nbsp;Leckie (The&nbsp;University&nbsp;of&nbsp;Melbourne) <br>
    <div class='button-group'>
        <span class='button' id='spot-100'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2502.19755'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-100'>
        Effective out-of-distribution (OOD) detection is crucial for the safe deployment of machine learning models in real-world scenarios. However, recent work has shown that OOD detection methods are vulnerable to adversarial attacks, potentially leading to critical failures in high-stakes applications. This discovery has motivated work on robust OOD detection methods that are capable of maintaining performance under various attack settings. Prior approaches have made progress on this problem but face a number of limitations: often only exhibiting robustness to attacks on OOD data or failing to maintain strong clean performance. In this work, we adapt an existing robust classification framework, TRADES, extending it to the problem of robust OOD detection and discovering a novel objective function. Recognising the critical importance of a strong clean/robust trade-off for OOD detection, we introduce an additional loss term which boosts classification and detection performance. Our approach, called HALO (Helper-based AdversariaL OOD detection), surpasses existing methods and achieves state-of-the-art performance across a number of datasets and attack settings. Extensive experiments demonstrate an average AUROC improvement of 3.15 in clean settings and 7.07 under adversarial attacks when compared to the next best method. Furthermore, HALO exhibits resistance to transferred attacks, offers tuneable performance through hyper-parameter selection, and is compatible with existing OOD detection frameworks out-of-the-box, leaving open the possibility of future performance gains. 
    </blockquote>
    <script>
        $("#spot-100").click(function(){
            $("#abstract-100").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Targeted Manifold Manipulation Against Adversarial Attacks</em> <br> 
    Banibrata&nbsp;Ghosh, Haripriya&nbsp;Harikumar, Svetha&nbsp;Venkatesh, Santu&nbsp;Rana (Deakin&nbsp;University) <br>
    <div class='button-group'>
        <span class='button' id='spot-123'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-123'>
        Adversarial attacks on deep models are often guaranteed to find a small and innocuous perturbation to easily alter class label of a test input. We use a novel Targeted Manifold Manipulation (TMM) approach to direct the gradients from the genuine data manifold toward carefully planted traps during such adversarial attacks. The traps are assigned an additional class label (Trapclass) to make the attacks falling in them easily identifiable. Whilst low-perturbation budget attacks will necessarily end up in the traps, high-perturbation budget attacks may escape but only end up far away from the data manifold. Since our manifold manipulation is enforced only locally, we show that such out-of-distribution data can be easily detected by noting the absence of traps around them. Our <strong>detection algorithm, denoted as TMM-Def</strong> avoids learning a separate model for attack detection and thus remains semantically aligned with the original classifier. Further, since we manipulate the adversarial distribution, it avoids the fundamental difficulty associated with overlapping distributions of clean and attack samples for usual, unmanipulated models. We use nine state-of-the-art adversarial attacks with six well-known image datasets to evaluate our proposed defense. Our results show that the proposed method can detect <em>\sim</em>99% attacks whilst also being robust to semantic-preserving, transformations, and adaptive attacks. 
    </blockquote>
    <script>
        $("#spot-123").click(function(){
            $("#abstract-123").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>SEA: Shareable and Explainable Attribution for Query-based Black-box Attacks</em> <br> 
    Yue&nbsp;Gao (University&nbsp;of&nbsp;Wisconsin-Madison), Ilia&nbsp;Shumailov (University&nbsp;of&nbsp;Oxford), Kassem&nbsp;Fawaz (University&nbsp;of&nbsp;Wisconsin-Madison) <br>
    <div class='button-group'>
        <span class='button' id='spot-125'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2308.11845'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-125'>
        Machine Learning (ML) systems are vulnerable to adversarial examples, particularly those from query-based black-box attacks. Despite various efforts to detect and prevent such attacks, our ML systems are still at risk, demanding a more comprehensive approach to security, including logging, analyzing, and sharing evidence. While classic security benefits from well-established forensics and intelligence sharing, ML has yet to find a way to profile its attackers and share information about them. In response, this paper introduces SEA, a novel ML security system to characterize black-box attacks on ML systems for forensic purposes and to facilitate human-explainable intelligence sharing. SEA leverages Hidden Markov Models to attribute the observed query sequence to known attacks. It thus understands the attack's progression rather than just focusing on the final adversarial examples. Our evaluations reveal that SEA is effective at attack attribution, even on the second incident, and is robust to adaptive strategies designed to evade forensic analysis. SEA's explanations of the attack's behavior allow us even to fingerprint specific minor bugs in widely used attack libraries. For example, we discover that the SignOPT and Square attacks in ART v1.14 send over 50% duplicated queries. We thoroughly evaluate SEA on a variety of settings and demonstrate that it can recognize the same attack with more than 90% Top-1 and 95% Top-3 accuracy. Finally, we demonstrate how SEA generalizes to other domains like text classification. 
    </blockquote>
    <script>
        $("#spot-125").click(function(){
            $("#abstract-125").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>SpaNN: Detecting Multiple Adversarial Patches on CNNs by Spanning Saliency Thresholds</em> <br> 
    Mauricio&nbsp;Byrd Victorica, György&nbsp;Dán, Henrik&nbsp;Sandberg (KTH&nbsp;Royal&nbsp;Institute&nbsp;of&nbsp;Technology) <br>
    <div class='button-group'>
        <span class='button' id='spot-142'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-142'>
        State-of-the-art convolutional neural network models for object detection and image classification are vulnerable to physically realizable adversarial perturbations, such as patch attacks. Existing defenses have focused, implicitly or explicitly, on single-patch attacks, rendering them computationally infeasible or inefficient against attacks consisting of multiple patches in the worst cases, or leaving their sensitivity to the number of patches as an open question. In this work, we propose SpaNN, an attack detector whose computational complexity is independent of the expected number of adversarial patches. The key novelty of the proposed detector is that it builds an ensemble of binarized feature maps by applying a set of saliency thresholds to the neural activations of the first convolutional layer of the victim model. It then performs clustering on the ensemble and uses the cluster features as the input to a classifier for attack detection. Contrary to existing detectors, SpaNN does not rely on a fixed saliency threshold for identifying adversarial regions, which makes it robust against white box adversarial attacks.  We evaluate SpaNN on four widely used data sets for object detection and classification, and our results show that SpaNN outperforms state-of-the-art defenses by up to 15 and 27 percentage points in the case of object detection and the case of image classification, respectively. Our code will be made available upon publication. 
    </blockquote>
    <script>
        $("#spot-142").click(function(){
            $("#abstract-142").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='lunch'> <div class='slot-time'>12:20&ndash;13:30</div> <a class='anchor' name='04101220'></a> <div class='slot-title lunch'>Lunch Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>13:30&ndash;14:30</div> <a class='anchor' name='04101330'></a> <div class='slot-title session'>Session: Machine Unlearning</div>
</h5>
<p class='session-chair'>Session Chair: <b>Yugeng Liu</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Verifiable and Provably Secure Machine Unlearning</em> <br> 
    Thorsten&nbsp;Eisenhofer (BIFOLD&nbsp;&&nbsp;TU&nbsp;Berlin), Doreen&nbsp;Riepel (University&nbsp;of&nbsp;California&nbsp;San&nbsp;Diego), Varun&nbsp;Chandrasekaran (University&nbsp;of&nbsp;Illinois&nbsp;Urbana-Champaign), Esha&nbsp;Ghosh (Microsoft&nbsp;Research), Olga&nbsp;Ohrimenko (The&nbsp;University&nbsp;of&nbsp;Melbourne), Nicolas&nbsp;Papernot (University&nbsp;of&nbsp;Toronto&nbsp;and&nbsp;Vector&nbsp;Institute) <br>
    <div class='button-group'>
        <span class='button' id='spot-89'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2210.09126'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-89'>
        Machine unlearning aims to remove points from the training dataset of a machine learning model after training: e.g., when a user requests their data to be deleted. While many unlearning methods have been proposed, none of them enable users to audit the procedure. Furthermore, recent work shows a user is unable to verify whether their data was unlearnt from an inspection of the model parameter alone. Rather than reasoning about parameters, we propose to view verifiable unlearning as a security problem. To this end, we present the first cryptographic definition of verifiable unlearning to formally capture the guarantees of an unlearning system. In this framework, the server first computes a proof that the model was trained on a dataset D. Given a user's data point d requested to be deleted, the server updates the model using an unlearning algorithm. It then provides a proof of the correct execution of unlearning and that d is not part of D', where D' is the new training dataset (i.e., d has been removed). Our framework is generally applicable to different unlearning techniques that we abstract as admissible functions. We instantiate a protocol in the framework, based on cryptographic assumptions, using SNARKs and hash chains. Finally, we implement the protocol for three different unlearning techniques and validate its feasibility for linear regression, logistic regression, and neural networks. 
    </blockquote>
    <script>
        $("#spot-89").click(function(){
            $("#abstract-89").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Inexact Unlearning Needs More Careful Evaluations to Avoid a False Sense of Privacy</em> <br> 
    Jamie&nbsp;Hayes (Google&nbsp;Deepmind), Amr&nbsp;Khalifa, Ilia&nbsp;Shumailov, Nicolas&nbsp;Papernot, Eleni&nbsp;Triantafillou (Google&nbsp;DeepMind) <br>
    <div class='button-group'>
        <span class='button' id='spot-91'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2403.01218'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-91'>
        The high cost of model training makes it increasingly desirable to develop techniques for unlearning.  These techniques seek to remove the influence of a training example without having to retrain the model from scratch. Intuitively, once a model has unlearned, an adversary that interacts with the model should no longer be able to tell whether the unlearned example was included in the model's training set or not. In the privacy literature, this is known as membership inference.  In this work, we discuss adaptations of Membership Inference Attacks (MIAs) to the setting of unlearning (leading to their ``U-MIA'' counterparts). We propose a categorization of existing U-MIAs into ``population U-MIAs'', where the same attacker is instantiated for all examples, and ``per-example U-MIAs'', where a dedicated attacker is instantiated for each example.  We show that the latter category, wherein the attacker tailors its membership prediction to each example under attack, is significantly stronger. Indeed, our results show that the commonly used U-MIAs in the unlearning literature overestimate the privacy protection afforded by existing unlearning techniques on both vision and language models.  Our investigation reveals a large variance in the vulnerability of different examples to per-example U-MIAs.  In fact, several unlearning algorithms lead to a reduced vulnerability for some, but not all, examples that we wish to unlearn, at the expense of increasing it for other examples.  Notably, we find that the privacy protection for the remaining training examples may worsen as a consequence of unlearning.  We also discuss the fundamental difficulty of equally protecting all examples using existing unlearning schemes, due to the different rates at which different examples are unlearned.  We demonstrate that naive attempts at tailoring unlearning stopping criteria to different examples fail to alleviate these issues. 
    </blockquote>
    <script>
        $("#spot-91").click(function(){
            $("#abstract-91").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Position: LLM Unlearning Benchmarks are Weak Measures of Progress</em> <br> 
    Pratiksha&nbsp;Thaker, Shengyuan&nbsp;Hu, Neil&nbsp;Kale, Yash&nbsp;Maurya, Zhiwei Steven&nbsp;Wu, Virginia&nbsp;Smith (CMU) <br>
    <div class='button-group'>
        <span class='button' id='spot-160'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-160'>
        Unlearning methods have the potential to improve the privacy and safety of large language models (LLMs) by removing sensitive or harmful information post hoc. The LLM unlearning research community has increasingly turned toward empirical benchmarks to assess the effectiveness of such methods. In this paper, we find that existing benchmarks provide an overly optimistic and potentially misleading view on the effectiveness of candidate unlearning methods. By introducing simple, benign modifications to a number of popular benchmarks, we expose instances where supposedly unlearned information remains accessible, or where the unlearning process has degraded the model’s performance on retained information to a much greater extent than indicated by the original benchmark. We identify that existing benchmarks are particularly vulnerable to modifications that introduce even loose dependencies between the forget and retain information. Further, we show that ambiguity in unlearning targets in existing benchmarks can easily lead to the design of methods that overfit to the given test queries. Based on our findings, we urge the community to be cautious when interpreting benchmark results as reliable measures of progress, and we provide several recommendations to guide future LLM unlearning research. 
    </blockquote>
    <script>
        $("#spot-160").click(function(){
            $("#abstract-160").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>On the Reliability of Membership Inference Attacks</em> <br> 
    Amrita&nbsp;Roy Chowdhury (University&nbsp;of&nbsp;Michigan,&nbsp;Ann&nbsp;Arbor), Zhifeng&nbsp;Kong, Kamalika&nbsp;Chaudhuri (UCSD) <br>
    <div class='button-group'>
        <span class='button' id='spot-162'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-162'>
        A membership inference (MI) attack predicts whether a data point was used for training a machine learning (ML) model. MI attacks are currently the most widely deployed attack for auditing privacy of a ML model. A recent work by Thudi et. al.  show that approximate machine unlearning is ill-defined. For this, they introduce the notion of forgeability  where using forged datasets, one could unlearn without modifying the model at all. In this paper, we show a connection between machine unlearning and membership inferencing. Specifically, we study <em>how to leverage forgeability to repudiate claims on membership inferencing</em>.  We show that the ability to forge enables the dataset owner to  construct a <em>Witness-of-Repudiation</em> (WoR) which empowers the dataset owner to plausibly <em>repudiate</em> the predictions of an MI attack. This casts a doubt on the reliability of MI attacks in practice. Our empirical evaluations show that it is possible to construct WoRs~efficiently. 
    </blockquote>
    <script>
        $("#spot-162").click(function(){
            $("#abstract-162").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='coffee'> <div class='slot-time'>14:30&ndash;14:50</div> <a class='anchor' name='04101430'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='competitions'> <div class='slot-time'>14:50&ndash;15:20</div> <a class='anchor' name='04101450'></a> <div class='slot-title competitions'>Competitions</div>
</h5>
<p class='session-chair'>Session Chair: <b>Konrad Rieck</b></p>
<ul class='paper-list program'>
<li class='paper-item program competition'>
    <em class='paper-title'>🏁 Inference Attacks Against Document VQA</em> <br>
    <div class='button-group'>
    <a class='button' href="/competitions/#competition2"><small>📃</small> Abstract</a>
    <a class='button' href="https://benchmarks.elsa-ai.eu/?ch=2&com=introduction"><small>🌐</small> Website</a>
    </div>
</li><li class='paper-item program competition'>
    <em class='paper-title'>🏁 Robust Android Malware Detection Competition</em> <br>
    <div class='button-group'>
    <a class='button' href="/competitions/#competition4"><small>📃</small> Abstract</a>
    <a class='button' href="https://ramd-competition.github.io"><small>🌐</small> Website</a>
    </div>
</li></ul>

<h5 class='break'> <div class='slot-time'>15:20&ndash;15:40</div> <a class='anchor' name='04101520'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>15:40&ndash;16:40</div> <a class='anchor' name='04101540'></a> <div class='slot-title session'>Session: Private Algorithms</div>
</h5>
<p class='session-chair'>Session Chair: <b>Saeyoung Rho</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Streaming Private Continual Counting via Binning</em> <br> 
    Joel Daniel&nbsp;Andersson, Rasmus&nbsp;Pagh (University&nbsp;of&nbsp;Copenhagen) <br>
    <div class='button-group'>
        <span class='button' id='spot-156'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2412.07093'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-156'>
        In differential privacy, <em>continual observation</em> refers to problems in which we wish to continuously release a function of a dataset that is revealed one element at a time. The challenge is to maintain a good approximation while keeping the combined output over all time steps differentially private. In the special case of <em>continual counting</em> we seek to approximate a sum of binary input elements. This problem has received considerable attention lately, in part due to its relevance in implementations of differentially private stochastic gradient descent. <em>Factorization mechanisms</em> are the leading approach to continual counting but the best such mechanisms do not work well in <em>streaming</em> settings since they require space proportional to the size of the input. In this paper we present a simple approach to approximating factorization mechanisms in low space via <em>binning</em>, where adjacent matrix entries with similar values are changed to be identical in such a way that a matrix-vector product can be maintained in sublinear space. Our approach has provable sublinear space guarantees for a class of lower triangular matrices whose entries are monotonically decreasing away from the diagonal. We show empirically that even with very low space usage we are able to closely match, and sometimes surpass, the performance of asymptotically optimal factorization mechanisms. Recently, and independently of our work, Dvijotham et al.~have also suggested an approach to implementing factorization mechanisms in a streaming setting. Their work differs from ours in several respects: It only addresses factorization into <em>Toeplitz</em> matrices, only considers <em>maximum</em> error, and uses a different technique based on rational function approximation that seems less versatile than our binning approach. 
    </blockquote>
    <script>
        $("#spot-156").click(function(){
            $("#abstract-156").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Correlated Privacy Mechanisms for Differentially Private Distributed Mean Estimation</em> <br> 
    Sajani&nbsp;Vithana (Harvard&nbsp;University), Viveck R.&nbsp;Cadambe (Georgia&nbsp;Institute&nbsp;of&nbsp;Technology), Flavio P.&nbsp;Calmon (Harvard&nbsp;University), Haewon&nbsp;Jeong (University&nbsp;of&nbsp;California,&nbsp;Santa&nbsp;Barbara) <br>
    <div class='button-group'>
        <span class='button' id='spot-173'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2407.03289'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-173'>
        Differentially private distributed mean estimation (DP-DME) is a fundamental building block in privacy-preserving federated learning, where a central server estimates the mean of <em>d</em>-dimensional vectors held by <em>n</em> users while ensuring <em>(ε,\delta)</em>-DP. Local differential privacy (LDP) and distributed DP with secure aggregation (SecAgg) are the most common notions of DP used in DP-DME settings with an untrusted server. LDP provides strong resilience to dropouts, colluding users, and adversarial attacks, but suffers from poor utility. In contrast, SecAgg-based DP-DME achieves an <em>O(n)</em> utility gain over LDP in DME, but requires increased communication and computation overheads and complex multi-round protocols to handle dropouts and attacks. In this work, we present a generalized framework for DP-DME, that captures LDP and SecAgg-based mechanisms as extreme cases. Our framework provides a foundation for developing and analyzing a variety of DP-DME protocols that leverage correlated privacy mechanisms across users. To this end, we propose CorDP-DME, a novel DP-DME mechanism based on the correlated Gaussian mechanism, that spans the gap between DME with LDP and distributed DP. We prove that CorDP-DME offers a favorable balance between utility and resilience to dropout and collusion. We provide an information-theoretic analysis of CorDP-DME, and derive theoretical guarantees for utility under any given privacy parameters and dropout/colluding user thresholds. Our results demonstrate that (anti) correlated Gaussian DP mechanisms can significantly improve utility in mean estimation tasks compared to LDP &ndash; even in adversarial settings &ndash; while maintaining better resilience to dropouts and attacks compared to distributed DP. 
    </blockquote>
    <script>
        $("#spot-173").click(function(){
            $("#abstract-173").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Private Selection with Heterogeneous Sensitivities</em> <br> 
    Daniela&nbsp;Antonova, Allegra&nbsp;Latimer, Audra&nbsp;McMillan (Apple), Lorenz&nbsp;Wolf (University&nbsp;College&nbsp;London) <br>
    <div class='button-group'>
        <span class='button' id='spot-185'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2501.05309'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-185'>
        Differentially private (DP) selection involves choosing a high-scoring candidate from a finite candidate pool, where each score depends on a sensitive dataset. This problem arises naturally in a variety of contexts including model selection, hypothesis testing, and within many DP algorithms. Classical methods, such as Report Noisy Max (RNM) [5], assume all candidates' scores are equally sensitive to changes in a single individual's data, but this often isn’t the case. To address this, algorithms like the Generalised Exponential Mechanism (GEM) [19] leverage variability in candidate sensitivities. However, we observe that while these algorithms can outperform RNM in some situations, they may underperform in others—they can even perform worse than random selection. In this work, we explore how the distribution of scores and sensitivities impacts DP selection mechanisms. In all settings we study, we find that there exists a mechanism that utilises heterogeneity in the candidate sensitivities that outperforms standard mechanisms like RNM. However, no single mechanism uniformly outperforms RNM. We propose using the correlation between the scores and sensitivities as the basis for deciding which DP selection mechanism to use. Further, we design a slight variant of GEM that generally performs well whenever GEM performs poorly. 
    </blockquote>
    <script>
        $("#spot-185").click(function(){
            $("#abstract-185").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Equilibria of Data Marketplaces with Privacy-Aware Sellers under Endogenous Privacy Costs</em> <br> 
    Diptangshu&nbsp;Sen (Georgia&nbsp;Institute&nbsp;of&nbsp;Technology), Jingyan&nbsp;Wang (Toyota&nbsp;Technological&nbsp;Institute&nbsp;at&nbsp;Chicago), Juba&nbsp;Ziani (Georgia&nbsp;Institute&nbsp;of&nbsp;Technology) <br>
    <div class='button-group'>
        <span class='button' id='spot-113'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2402.08826'><small>📚</small> Arxiv</a> <span class='button no-border no-link'>⚠️ Video talk</span>
    </div>
    <blockquote class='paper-abstract' id='abstract-113'>
        We study a two-sided online data ecosystem comprised of an online platform, users on the platform, and downstream data buyers. The buyers can buy user data on the platform to run a statistic or machine learning task. Potential users decide whether to join by looking at the trade-off between i) their benefit from joining the platform and interacting with other users and ii) the privacy costs they incur from sharing their data.  In light of the rapidly changing user privacy attitudes, we introduce a novel modeling element for two-sided data platforms: the privacy costs of users are endogenous and depend on the number of downstream buyers who purchase and access their data. Then, we characterize marketplace equilibria in certain simple settings. In particular, we provide a full characterization in two variants of our model that correspond to different utility functions for the users: i) when each user gets a constant benefit for participating on the platform and ii) when each user's benefit is linearly increasing in the number of other users that participate. In both variants, equilibria in our setting are significantly different from equilibria when privacy costs are exogenous and fixed, the most significant point of difference being that under exogenous privacy costs, the user-side participation rate is completely independent of the platform's price and the buyer-side decisions and thus can never be improved without investing in improving the quality of service offered. This highlights the importance of taking endogeneity in privacy costs into account. Finally, we provide simulations and semi-synthetic experiments to extend our results to more general assumptions; we experiment with different distributions of users' privacy costs and different functional forms of the users' utilities for joining the platform. 
    </blockquote>
    <script>
        $("#spot-113").click(function(){
            $("#abstract-113").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>16:40&ndash;17:00</div> <a class='anchor' name='04101640'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>17:00&ndash;17:45</div> <a class='anchor' name='04101700'></a> <div class='slot-title session'>Session: Vision and Perception</div>
</h5>
<p class='session-chair'>Session Chair: <b>Adam Dziedzic</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Adversarially Robust CLIP Models Can Induce Better (Robust) Perceptual Metrics</em> <br> 
    Francesco&nbsp;Croce (EPFL), Christian&nbsp;Schlarmann, Naman Deep&nbsp;Singh, Matthias&nbsp;Hein (University&nbsp;of&nbsp;Tuebingen) <br>
    <div class='button-group'>
        <span class='button' id='spot-90'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2502.11725'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-90'>
        Measuring perceptual similarity is a key tool in computer vision. In recent years perceptual metrics based on features extracted from neural networks with large and diverse training sets, e.g. CLIP, have become popular. At the same time, the metrics extracted from features of neural networks are not adversarially robust. In this paper we show that adversarially robust CLIP models, called \rclipf, obtained by unsupervised adversarial finetuning induce a <em>better</em> and <em>adversarially robust</em> perceptual metric that outperforms existing metrics in a zero-shot setting, and further matches the performance of state-of-the-art metrics while being robust after fine-tuning. Moreover, our perceptual metric achieves strong performance on related task such as robust image-to-image retrieval, which becomes especially relevant when applied to ``Not Safe for Work'' (NSFW) content detection and dataset filtering. While standard perceptual metrics can be easily attacked by a small perturbation completely degrading NSFW detection, our robust perceptual metric maintains high accuracy under an attack while having similar performance for unperturbed images. Finally, perceptual metrics induced by robust CLIP models have higher interpretability: feature inversion can show which images are considered similar, while text inversion can find what images are associated to a given prompt. This also allows us to visualize the very rich visual concepts learned by a CLIP model, including memorized persons, paintings and complex queries. 
    </blockquote>
    <script>
        $("#spot-90").click(function(){
            $("#abstract-90").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Err on the Side of Texture: Texture Bias on Real Data</em> <br> 
    Blaine&nbsp;Hoak, Ryan&nbsp;Sheatsley, Patrick&nbsp;McDaniel (University&nbsp;of&nbsp;Wisconsin-Madison) <br>
    <div class='button-group'>
        <span class='button' id='spot-120'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2412.10597'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-120'>
        Bias significantly undermines both the accuracy and trustworthiness of machine learning models. To date, one of the strongest biases observed in image classification models is texture bias where models overly rely on texture information rather than shape information. Yet, existing approaches for measuring and mitigating texture bias have not been able to capture how textures impact model robustness in real-world settings. In this work, we introduce the Texture Association Value (TAV), a novel metric that quantifies how strongly models rely on the presence of specific textures when classifying objects. Leveraging TAV, we demonstrate that model accuracy and robustness are heavily influenced by texture. Our results show that texture bias explains the existence of natural adversarial examples, where over 90% of these samples contain textures that are misaligned with the learned texture of their true label, resulting in confident mispredictions. 
    </blockquote>
    <script>
        $("#spot-120").click(function(){
            $("#abstract-120").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>ColorSense: A Study on Color Vision in Machine Visual Recognition</em> <br> 
    Ming-Chang&nbsp;Chiu, Yingfei&nbsp;Wang (University&nbsp;of&nbsp;Southern&nbsp;California), Derrick Eui Gyu&nbsp;Kim (Brandeis&nbsp;University), Pin-Yu&nbsp;Chen (IBM&nbsp;Research), Xuezhe&nbsp;Ma (University&nbsp;of&nbsp;Southern&nbsp;California) <br>
    <div class='button-group'>
        <span class='button' id='spot-183'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2212.08650'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-183'>
        Color vision is essential for human visual perception, but its impact on machine perception is still underexplored. There has been an intensified demand for understanding its role in machine perception for safety-critical tasks such as assistive driving and surgery but lacking suitable datasets. To fill this gap, we curate multipurpose datasets ColorSense, by collecting 110,000 non-trivial human annotations of foreground and background color labels from popular visual recognition benchmarks. To investigate the impact of color vision on machine perception, we assign each image a color discrimination level based on its dominant foreground and background colors and use it to study the impact of color vision on machine perception. We validate the use of our datasets by demonstrating that the level of color discrimination has a dominating effect on the performance of mainstream machine perception models. Specifically, we examine the perception ability of machine vision by considering key factors such as model architecture, training objective, model size, training data, and task complexity. Furthermore, to investigate how color and environmental factors affect the robustness of visual recognition in machine perception, we integrate our ColorSense datasets with image corruptions and perform a more comprehensive visual perception evaluation. We jointly analyze the impact of color vision and image corruption on machine perception. Our findings suggest that "object recognition" tasks such as "classification" and "localization" are susceptible to color vision bias, especially for high-stakes cases such as vehicle classes, and advanced mitigation techniques such as data augmentation and so on only give marginal improvement. Our analyses highlight the need for new approaches toward the performance evaluation of machine perception models in real-world applications. Lastly, we present various potential applications of "ColorSense" such as studying spurious correlations. 
    </blockquote>
    <script>
        $("#spot-183").click(function(){
            $("#abstract-183").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<br/><hr>

<a class='anchor' name='0411'></a>
#### <div class='day-title'>Friday, April 11, 2025</div>
<h5 class='keynote'> <div class='slot-time'>09:00&ndash;09:40</div> <a class='anchor' name='04110900'></a> <div class='slot-title keynote'>Keynote 3</div>
</h5>
<p class='session-chair'>Session Chair: <b>Amartya Sanyal</b></p>
<ul class='paper-list program'>
<li class='paper-item program keynote'>
    <em class='paper-title'>Artificial Intelligence: Should you trust it?</em> <br> 
    Matt Turek (Defense Advanced Research Agency)<br>
    <div class='button-group'>
    <a href="/keynotes/#keynote3" class='button'><small>📃</small> Abstract</a>
    <a href="https://www.darpa.mil/about/people/matt-turek" class='button'><small>👤</small> Speaker</a>
    </div>
</li> 
</ul>

<h5 class='coffee'> <div class='slot-time'>09:40&ndash;10:00</div> <a class='anchor' name='04110940'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>10:00&ndash;11:00</div> <a class='anchor' name='04111000'></a> <div class='slot-title session'>Session: Fairness and Bias</div>
</h5>
<p class='session-chair'>Session Chair: <b>Rasmus Pagh</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>Fair Decentralized Learning</em> <br> 
    Sayan&nbsp;Biswas, Anne-Marie&nbsp;Kermarrec, Rishi&nbsp;Sharma, Thibaud&nbsp;Trinca, Martijn&nbsp;de Vos (EPFL) <br>
    <div class='button-group'>
        <span class='button' id='spot-105'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2410.02541'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-105'>
        Decentralized learning (DL) is an emerging approach that enables nodes to collaboratively train a machine learning model without sharing raw data. In many application domains, such as healthcare, this approach faces challenges due to the high level of heterogeneity in the training data's feature space. Such feature heterogeneity lowers model utility and negatively impacts fairness, particularly for nodes with under-represented training data. In this paper, we introduce <em>Facade</em>, a clustering-based DL algorithm specifically designed for fair model training when the training data exhibits several distinct features. The challenge of <em>Facade</em> is to assign nodes to clusters, one for each feature, based on the similarity in the features of their local data, without requiring individual nodes to know apriori which cluster they belong to. <em>Facade</em> (1) dynamically assigns nodes to their appropriate clusters over time, and (2) enables nodes to collaboratively train a specialized model for each cluster in a fully decentralized manner. We theoretically prove the convergence of <em>Facade</em>, implement our algorithm, and compare it against three state-of-the-art baselines. Our experimental results on three datasets demonstrate the superiority of our approach in terms of model accuracy and fairness compared to all three competitors. Compared to the best-performing baseline, <em>Facade</em> on the CIFAR-10 dataset also reduces communication costs by 32.3% to reach a target accuracy when cluster sizes are imbalanced. 
    </blockquote>
    <script>
        $("#spot-105").click(function(){
            $("#abstract-105").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>When mitigating bias is unfair: multiplicity and arbitrariness in algorithmic group fairness</em> <br> 
    Natasa&nbsp;Krco (Imperial&nbsp;College,&nbsp;London,&nbsp;United&nbsp;Kingdom), Thibault&nbsp;Laugel, Vincent&nbsp;Grari (AXA,&nbsp;Paris,&nbsp;France), Jean-Michel&nbsp;Loubes (Institut&nbsp;de&nbsp;Mathématiques&nbsp;de&nbsp;Toulouse,&nbsp;Université&nbsp;Paul&nbsp;Sabatier,&nbsp;Toulouse,&nbsp;France), Marcin&nbsp;Detyniecki (AXA,&nbsp;Paris,&nbsp;France) <br>
    <div class='button-group'>
        <span class='button' id='spot-128'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-128'>
        Most research on fair machine learning has prioritized optimizing criteria such as Demographic Parity and Equalized Odds. Despite these efforts, there remains a limited understanding of how different bias mitigation strategies affect individual predictions and whether they introduce arbitrariness into the debiasing process. This paper addresses these gaps by exploring whether models that achieve comparable fairness and accuracy metrics impact the same individuals and mitigate bias in a consistent manner. We introduce the FRAME (FaiRness Arbitrariness and Multiplicity Evaluation) framework, which evaluates bias mitigation through five dimensions: Impact Size (how many people were affected), Change Direction (positive versus negative changes), Decision Rates (impact on models’ acceptance rates), Affected Subpopulations (who was affected), and Neglected Subpopulations (where unfairness persists). This framework is intended to help practitioners understand the impacts of debiasing processes and make better-informed decisions regarding model selection. Applying FRAME to various bias mitigation approaches across key datasets allows us to exhibit significant differences in the behaviors of debiasing methods. These findings highlight the limitations of current fairness criteria and the inherent arbitrariness in the debiasing process. 
    </blockquote>
    <script>
        $("#spot-128").click(function(){
            $("#abstract-128").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Minimax Group Fairness in Strategic Classification</em> <br> 
    Emily&nbsp;Diana (CMU), Saeed&nbsp;Sharifi-Malvajerdi, Ali&nbsp;Vakilian (TTIC) <br>
    <div class='button-group'>
        <span class='button' id='spot-155'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-155'>
        In strategic classification, agents manipulate their features, at a cost, to receive a positive classification outcome from the learner's classifier. The goal of the learner in such settings is to learn a classifier that is robust to strategic manipulations. While the majority of works in this domain consider accuracy as the primary objective of the learner, in this work, we consider learning objectives that have group fairness guarantees in addition to accuracy guarantees. We work with the minimax group fairness notion that asks for minimizing the maximal group error rate across population groups.  We formalize a fairness-aware Stackelberg game between a population of agents consisting of several groups, with each group having its own cost function, and a learner in the agnostic PAC setting in which the learner is working with a hypothesis class H. When the cost functions of the agents are separable, we show the existence of an efficient algorithm that finds an approximately optimal deterministic classifier for the learner when the number of groups is small. This algorithm remains efficient, both statistically and computationally, even when the hypothesis class H is the set of all classifiers. We then consider cost functions that are not necessarily separable and show the existence of oracle-efficient algorithms that find approximately optimal randomized classifiers for the learner when H has finite strategic VC dimension. These algorithms work under the assumption that the learner is fully transparent: the learner draws a classifier from its distribution (randomized classifier) before the agents best respond. We highlight the effectiveness of such transparency in developing oracle-efficient algorithms. We conclude with verifying the efficacy of our algorithms on real data by conducting an experimental analysis. 
    </blockquote>
    <script>
        $("#spot-155").click(function(){
            $("#abstract-155").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>SoK: Fair Clustering: Critique, Caveats, and Future Directions</em> <br> 
    John&nbsp;Dickerson (University&nbsp;of&nbsp;Maryland), Seyed&nbsp;Esmaeili (University&nbsp;of&nbsp;Chicago), Jamie&nbsp;Morgenstern, Claire Jie&nbsp;Zhang (University&nbsp;of&nbsp;Washington) <br>
    <div class='button-group'>
        <span class='button' id='spot-77'><small>📃</small> Abstract</span>   <span class='button no-border no-link'>⚠️ Video talk</span>
    </div>
    <blockquote class='paper-abstract' id='abstract-77'>
        Clustering is a fundamental problem in machine learning and operations research. Given the fact that fairness considerations have become of paramount importance in algorithm design, fairness in clustering has received significant attention from the research community. The literature on fair clustering has resulted in a collection of interesting fairness notions and elaborate algorithms. In this paper, we take a critical view of fair clustering, identifying a collection of ignored issues such as the lack of a clear utility characterization and the difficulty in accounting for the downstream effects of a fair clustering algorithm in machine learning settings. In some cases, we demonstrate examples where the application of a fair clustering algorithm can have significant negative impacts on social welfare. We end by identifying a collection of steps that would lead towards more impactful research in fair clustering. 
    </blockquote>
    <script>
        $("#spot-77").click(function(){
            $("#abstract-77").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>11:00&ndash;11:20</div> <a class='anchor' name='04111100'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>11:20&ndash;12:20</div> <a class='anchor' name='04111120'></a> <div class='slot-title session'>Session: Robustness and Transferability</div>
</h5>
<p class='session-chair'>Session Chair: <b>Kathrin Grosse</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>DART: A Principled Approach to Adversarially Robust Unsupervised Domain Adaptation</em> <br> 
    Yunjuan&nbsp;Wang (Johns&nbsp;Hopkins&nbsp;University), Hussein&nbsp;Hazimeh, Natalia&nbsp;Ponomareva, Alexey&nbsp;Kurakin, Ibrahim&nbsp;Hammoud (Google), Raman&nbsp;Arora (Johns&nbsp;Hopkins&nbsp;University) <br>
    <div class='button-group'>
        <span class='button' id='spot-2'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-2'>
        Distribution shifts and adversarial examples are two major challenges for deploying machine learning models. While these challenges have been studied individually, their combination is an important topic that remains relatively under-explored. In this work, we study the problem of adversarial robustness under a common setting of distribution shift – unsupervised domain adaptation (UDA). Specifically, given a labeled source domain DS and an unlabeled target domain DT with related but different distributions, the goal is to obtain an adversarially robust model for DT. The absence of target domain labels poses a unique challenge, as conventional adversarial robustness defenses cannot be directly applied to DT. To address this challenge, we first establish a generalization bound for the adversarial target loss, which consists of (i) terms related to the loss on the data, and (ii) a measure of worst-case domain divergence. Motivated by this bound, we develop a novel unified defense framework called Divergence Aware adveRsarial Training (DART), which can be used in conjunction with a variety of standard UDA methods; e.g., DANN (Ganin & Lempitsky, 2015). DART is applicable to general threat models, including the popular lp-norm model, and does not require heuristic regularizers or architectural changes. We also release DomainRobust: a testbed for evaluating robustness of UDA models to adversarial attacks. DomainRobust consists of 4 multi-domain benchmark datasets (with 46 source-target pairs) and 7 meta-algorithms with a total of 11 variants. Our large-scale experiments demonstrate that on average, DART significantly enhances model robustness on all benchmarks compared to the state of the art, while maintaining competitive standard accuracy. The relative improvement in robustness from DART reaches up to 29.2% on the source-target domain pairs considered. 
    </blockquote>
    <script>
        $("#spot-2").click(function(){
            $("#abstract-2").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Reliable Evaluation of Adversarial Transferability</em> <br> 
    Wenqian&nbsp;Yu (Wuhan&nbsp;University), Jindong&nbsp;Gu (University&nbsp;of&nbsp;Oxford), Zhijiang&nbsp;Li (Wuhan&nbsp;University), Philip&nbsp;Torr (University&nbsp;of&nbsp;Oxford) <br>
    <div class='button-group'>
        <span class='button' id='spot-7'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-7'>
        Adversarial examples (AEs) with small adversarial perturbations can mislead deep neural networks (DNNs) into wrong predictions. The AEs created on one DNN can also fool other networks. Over the last few years, the transferability of AEs has garnered significant attention as it is a crucial property for facilitating black-box attacks. Many approaches have been proposed to improve it and transferability of adversarial attacks across Convolutional Neural Networks (CNNs) is remarkably high, as attested by previous research. However, such evaluation methods are not reliable since all CNNs share some similar architectural biases. In this work, we re-evaluate 13 representative transferability-enhancing attack methods where we test on 18 popular models from 4 types of neural networks. Contrary to the prevailing belief, our reevaluation revealed that the adversarial transferability across these diverse network types is notably diminished, and there is no single AE that can be transferred to all popular models. The transferability rank of previous attacking methods changes when under our comprehensive evaluation. Based on our analysis, we propose a reliable benchmark including three evaluation protocols. We release our benchmark to facilitate future research, which includes code, model checkpoints, and evaluation protocols. 
    </blockquote>
    <script>
        $("#spot-7").click(function(){
            $("#abstract-7").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Hi-ALPS - An Experimental Robustness Quantification of Six LiDAR-based Object Detection Systems for Autonomous Driving</em> <br> 
    Alexandra&nbsp;Arzberger, Ramin Tavakoli&nbsp;Kolagari (Technische&nbsp;Hochschule&nbsp;Nürnberg&nbsp;Georg&nbsp;Simon&nbsp;Ohm) <br>
    <div class='button-group'>
        <span class='button' id='spot-57'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2503.17168'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-57'>
        Light Detection and Ranging (LiDAR) is an essential sensor technology for autonomous driving as it can capture high-resolution 3D data. As 3D object detection systems (OD) are able to interpret such point cloud data, they play a key role in the driving decisions of autonomous vehicles. Consequently, such 3D OD must be robust against all types of perturbations and must therefore be extensively tested. One approach is the use of Adversarial Examples (AE), which are small, sometimes sophisticated perturbations in the input data that change, i.e., falsify, the prediction of the OD. These perturbations are carefully designed based on the weaknesses of the OD. The robustness of the OD cannot be quantified with AE in general, because if the OD is vulnerable to a given attack, it is unclear whether this is due to the robustness of the OD or whether the AE algorithm produces particularly strong AE. The contribution of this work is Hi-ALPS&mdash;Hierarchical AE-based LiDAR Perturbation Level System, where a higher robustness of the OD is required to withstand the perturbations as the perturbation levels increase. In doing so, the Hi-ALPS levels successively implement heuristics followed by established AE approaches. In a series of comprehensive experiments using Hi-ALPS, we quantify the robustness of six state-of-the-art 3D OD under different types of perturbations. The results of the series of experiments show that none of the OD is robust at all Hi-ALPS levels; an important factor for the ranking is that human observers can still correctly recognize the perturbed objects, as the respective perturbations are small. In order to increase the robustness of the OD, we discuss the applicability of state-of-the-art countermeasures. In addition, we derive further suggestions for countermeasures based on our experimental results. 
    </blockquote>
    <script>
        $("#spot-57").click(function(){
            $("#abstract-57").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Timber! Poisoning Decision Trees</em> <br> 
    Stefano&nbsp;Calzavara, Lorenzo&nbsp;Cazzaro, Massimo&nbsp;Vettori (Università&nbsp;Ca'&nbsp;Foscari&nbsp;Venezia) <br>
    <div class='button-group'>
        <span class='button' id='spot-86'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2410.00862'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-86'>
        We present Timber, the first white-box poisoning attack targeting decision trees. Timber is based on a greedy attack strategy leveraging sub-tree retraining to efficiently estimate the damage performed by poisoning a given training instance. The attack relies on a tree annotation procedure which enables sorting training instances so that they are processed in increasing order of computational cost of sub-tree retraining. This sorting yields a variant of Timber supporting an early stopping criterion designed to make poisoning attacks more efficient and feasible on larger datasets. We also discuss an extension of Timber to traditional random forest models, which is useful because decision trees are normally combined into ensembles to improve their predictive power. Our experimental evaluation on public datasets shows that our attacks outperform existing baselines in terms of effectiveness, efficiency or both. Moreover, we show that two representative defenses can mitigate the effect of our attacks, but fail at effectively thwarting them. 
    </blockquote>
    <script>
        $("#spot-86").click(function(){
            $("#abstract-86").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='lunch'> <div class='slot-time'>12:20&ndash;13:30</div> <a class='anchor' name='04111220'></a> <div class='slot-title lunch'>Lunch Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>13:30&ndash;14:30</div> <a class='anchor' name='04111330'></a> <div class='slot-title session'>Session: Private Learning</div>
</h5>
<p class='session-chair'>Session Chair: <b>Franziska Boenisch</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>SoK: What Makes Private Learning Unfair?</em> <br> 
    Kai&nbsp;Yao, Marc&nbsp;Juarez (University&nbsp;of&nbsp;Edinburgh) <br>
    <div class='button-group'>
        <span class='button' id='spot-9'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2501.14414'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-9'>
        Differential privacy has emerged as the most studied framework for privacy-preserving machine learning. However, recent studies show that enforcing differential privacy guarantees can not only significantly degrade the utility of the model, but also amplify existing disparities in its predictive performance across demographic groups. Although there is extensive research on the identification of factors that contribute to this phenomenon, we still lack a complete understanding of the mechanisms through which differential privacy exacerbates disparities. The literature on this problem is muddled by varying definitions of fairness, differential privacy mechanisms, and inconsistent experimental settings, often leading to seemingly contradictory results.  This survey provides the first comprehensive overview of the factors that contribute to the disparate effect of training models with differential privacy guarantees. We discuss their impact and analyze their causal role in such a disparate effect. Our analysis is guided by a taxonomy that categorizes these factors by their position within the machine learning pipeline, allowing us to draw conclusions about their interaction and the feasibility of potential mitigation strategies. We find that factors related to the training dataset and the underlying distribution play a decisive role in the occurrence of disparate impact, highlighting the need for research on these factors to address the issue. 
    </blockquote>
    <script>
        $("#spot-9").click(function(){
            $("#abstract-9").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Differentially Private Active Learning: Balancing Effective Data Selection and Privacy</em> <br> 
    Kristian&nbsp;Schwethelm, Johannes&nbsp;Kaiser, Jonas&nbsp;Kuntzer (Technical&nbsp;University&nbsp;of&nbsp;Munich), Mehmet&nbsp;Yigitsoy (deepc&nbsp;GmbH), Daniel&nbsp;Rückert (Technical&nbsp;University&nbsp;of&nbsp;Munich,&nbsp;Imperial&nbsp;College&nbsp;London), Georgios&nbsp;Kaissis (Technical&nbsp;University&nbsp;of&nbsp;Munich,&nbsp;Helmholtz&nbsp;Munich) <br>
    <div class='button-group'>
        <span class='button' id='spot-27'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2410.00542'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-27'>
        Active learning (AL) is a widely used technique for optimizing data labeling in machine learning by iteratively selecting, labeling, and training on the most informative data. However, its integration with formal privacy-preserving methods, particularly differential privacy (DP), remains largely underexplored. While some works have explored differentially private AL for specialized scenarios like online learning, the fundamental challenge of combining AL with DP in standard learning settings has remained unaddressed, severely limiting AL's applicability in privacy-sensitive domains. This work addresses this gap by introducing differentially private active learning (DP-AL) for standard learning settings. We demonstrate that naively integrating DP-SGD training into AL presents substantial challenges in privacy budget allocation and data utilization. To overcome these challenges, we propose step amplification, which leverages individual sampling probabilities in batch creation to maximize data point participation in training steps, thus optimizing data utilization. Additionally, we investigate the effectiveness of various acquisition functions for data selection under privacy constraints, revealing that many commonly used functions become impractical. Our experiments on vision and natural language processing tasks show that DP-AL can improve performance for specific datasets and model architectures. However, our findings also highlight the limitations of AL in privacy-constrained environments, emphasizing the trade-offs between privacy, model accuracy, and data selection accuracy. 
    </blockquote>
    <script>
        $("#spot-27").click(function(){
            $("#abstract-27").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Choosing Public Datasets for Private Machine Learning via Gradient Subspace Distance</em> <br> 
    Xin&nbsp;Gu (Penn&nbsp;State&nbsp;University), Gautam&nbsp;Kamath (University&nbsp;of&nbsp;Waterloo), Steven&nbsp;Wu (Carnegie&nbsp;Mellon&nbsp;University) <br>
    <div class='button-group'>
        <span class='button' id='spot-116'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2303.01256'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-116'>
        Differentially private stochastic gradient descent privatizes model training by injecting noise into each iteration, where the noise magnitude increases with the number of model parameters. Recent works suggest that we can reduce the noise by leveraging public data for private machine learning, by projecting gradients onto a subspace prescribed by the public data. However, given a choice of public datasets, it is unclear why certain datasets perform better than others for a particular private task, or how to identify the best one. We provide a simple metric which measures a low-dimensional subspace distance between gradients of the public and private examples. We empirically demonstrate that it is well-correlated with resulting model utility when using the public and private dataset pair (i.e., trained model accuracy is monotone in the distance), and thus can be used to select an appropriate public dataset. We provide theoretical analysis demonstrating that the excess risk scales with this subspace distance. This distance is easy to compute and robust to modifications in the setting. 
    </blockquote>
    <script>
        $("#spot-116").click(function(){
            $("#abstract-116").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Learning with User-Level Differential Privacy under Fixed Compute Budgets</em> <br> 
    Zachary&nbsp;Charles, Arun&nbsp;Ganesh, Ryan&nbsp;McKenna, H. Brendan&nbsp;McMahan, Nicole&nbsp;Mitchell (Google&nbsp;Research), Krishna&nbsp;Pillutla (IIT&nbsp;Madras), Keith&nbsp;Rush (Google&nbsp;Research) <br>
    <div class='button-group'>
        <span class='button' id='spot-122'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-122'>
        We investigate practical and scalable algorithms for training machine learning models with user-level differential privacy (DP) in order to provably safeguard all the examples contributed by each user. Motivated by the application of large language model (LLM) fine-tuning, we analyze algorithms under fixed compute budgets, especially large budget settings. We study two variants of DP-SGD with: (1) example-level sampling (DP-SGD-ELS) and per-example gradient clipping, and (2) user-level sampling (DP-SGD-ULS) and per-user gradient clipping. We derive a novel user-level DP accountant that allows us to compute provably tight privacy guarantees for ELS. We show that for fixed compute and privacy budgets, ULS generally yields better results than ELS, especially when each user has a diverse collection of examples and the compute budget is large. We validate our findings through experiments in synthetic mean estimation and LLM fine-tuning tasks under fixed compute budgets. We find that ULS is significantly better in settings where either (1) strong privacy guarantees are required, or (2) the compute budget is large. Notably, our focus on scalability enables us to scale to models with hundreds of millions of parameters and datasets with hundreds of thousands of users. 
    </blockquote>
    <script>
        $("#spot-122").click(function(){
            $("#abstract-122").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='coffee'> <div class='slot-time'>14:30&ndash;14:50</div> <a class='anchor' name='04111430'></a> <div class='slot-title coffee'>Coffee Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>14:50&ndash;15:20</div> <a class='anchor' name='04111450'></a> <div class='slot-title session'>Session: Malware and Steganography</div>
</h5>
<p class='session-chair'>Session Chair: <b>Ilia Shumailov</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>ML-Based Behavioral Malware Detection Is Far From a Solved Problem</em> <br> 
    Yigitcan&nbsp;Kaya (UC&nbsp;Santa&nbsp;Barbara), Yizheng&nbsp;Chen (University&nbsp;of&nbsp;Maryland&nbsp;College&nbsp;Park), Marcus&nbsp;Botacin (Texas&nbsp;A&M&nbsp;University), Shoumik&nbsp;Saha (University&nbsp;of&nbsp;Maryland&nbsp;College&nbsp;Park), Fabio&nbsp;Pierazzi (King’s&nbsp;College&nbsp;London&nbsp;&&nbsp;University&nbsp;College&nbsp;London), Lorenzo&nbsp;Cavallaro (University&nbsp;College&nbsp;London), David&nbsp;Wagner (UC&nbsp;Berkeley), Tudor&nbsp;Dumitras (University&nbsp;of&nbsp;Maryland&nbsp;College&nbsp;Park) <br>
    <div class='button-group'>
        <span class='button' id='spot-82'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2405.06124'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-82'>
        Malware detection is a ubiquitous application of Machine Learning (ML) in security. In behavioral malware analysis, the detector relies on features extracted from program execution traces. The research literature has focused on detectors trained with features collected from sandbox environments and evaluated on samples also analyzed in a sandbox. However, in deployment, a malware detector at endpoint hosts often must rely on traces captured from endpoint hosts, not from a sandbox. Thus, there is a gap between the literature and real-world needs.   We present the first measurement study of the performance of ML-based malware detectors at real-world endpoints. Leveraging a dataset of sandbox traces and a dataset of in-the-wild program traces, we evaluate two scenarios: (i) an endpoint detector trained on sandbox traces (convenient and easy to train), and (ii) an endpoint detector trained on endpoint traces (more challenging to train, since we need to collect telemetry data). We discover a wide gap between the performance as measured using prior evaluation methods in the literature—over 90%—vs. expected performance in endpoint detection—about 20% (scenario (i)) to 50% (scenario (ii)). We characterize the ML challenges that arise in this domain and contribute to this gap, including label noise, distribution shift, and spurious features. Moreover, we show several techniques that achieve 5–30% relative performance improvements over the baselines. Our evidence suggests that applying detectors trained on sandbox data to endpoint detection is challenging. The most promising direction is training detectors directly on endpoint data, which marks a departure from current practice. To promote progress, we will facilitate researchers to perform realistic detector evaluations against our real-world dataset. 
    </blockquote>
    <script>
        $("#spot-82").click(function(){
            $("#abstract-82").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Provably Secure Covert Messaging Using Image-based Diffusion Processes</em> <br> 
    Luke&nbsp;Bauer, Wenxuan&nbsp;Bao, Vincent&nbsp;Bindschaedler (University&nbsp;of&nbsp;Florida) <br>
    <div class='button-group'>
        <span class='button' id='spot-104'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2503.10063'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-104'>
        We consider the problem of securely and robustly embedding covert messages into an image-based diffusion model's output. The sender and receiver want to exchange the maximum amount of information possible per diffusion sampled image while remaining undetected. The adversary wants to detect that such communication is taking place by identifying those diffusion samples that contain covert messages. To maximize robustness to transformations of the diffusion sample, a strategy is for the sender and the receiver to embed the message in the initial latents. We first show that prior work that attempted this is easily broken because their embedding technique alters the latents' distribution.  We then propose a straightforward method to embed covert messages in the initial latent without altering the distribution. We prove that our construction achieves indistinguishability to any probabilistic polynomial time adversary. Finally, we discuss and analyze empirically the tradeoffs between embedding capacity, message recovery rates, and robustness. We find that optimizing the inversion method for error correction is key to improve reliability. 
    </blockquote>
    <script>
        $("#spot-104").click(function(){
            $("#abstract-104").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='break'> <div class='slot-time'>15:20&ndash;15:40</div> <a class='anchor' name='04111520'></a> <div class='slot-title break'>Break</div>
</h5>
<h5 class='session'> <div class='slot-time'>15:40&ndash;16:40</div> <a class='anchor' name='04111540'></a> <div class='slot-title session'>Session: Differential Privacy</div>
</h5>
<p class='session-chair'>Session Chair: <b>Antti Honkela</b></p>
<ul class='paper-list program'>
<li class='paper-item program paper'>
    <em class='paper-title'>FairDP: Achieving Fairness Certification with Differential Privacy</em> <br> 
    Khang&nbsp;Tran (New&nbsp;Jersey&nbsp;Institute&nbsp;of&nbsp;Technology), Ferdinando&nbsp;Fioretto (University&nbsp;of&nbsp;Virginia), Issa&nbsp;Khalil (Qatar&nbsp;Computing&nbsp;Research&nbsp;Institute&nbsp;(QCRI),&nbsp;HBKU), My&nbsp;Thai (University&nbsp;of&nbsp;Florida), Linh&nbsp;Phan (University&nbsp;of&nbsp;Pennsylvania), Hai&nbsp;Phan (New&nbsp;Jersey&nbsp;Institute&nbsp;of&nbsp;Technology) <br>
    <div class='button-group'>
        <span class='button' id='spot-19'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2305.16474'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-19'>
        This paper introduces FairDP, a novel training mechanism designed to provide group fairness certification for the trained model's decisions, along with a differential privacy (DP) guarantee to protect training data. The key idea of FairDP is to train models for distinct individual groups independently, add noise to each group's gradient for data privacy protection, and progressively integrate knowledge from group models to formulate a comprehensive model that balances privacy, utility, and fairness in downstream tasks. By doing so, FairDP ensures equal contribution from each group while gaining control over the amount of DP-preserving noise added to each group's contribution. To provide fairness certification, FairDP leverages the DP-preserving noise to statistically quantify and bound fairness metrics. An extensive theoretical and empirical analysis using benchmark datasets validates the efficacy of FairDP and improved trade-offs between model utility, privacy, and fairness compared with existing methods. Our empirical results indicate that FairDP can improve fairness metrics by more than 65% on average while attaining marginal utility drop (less than 4% on average) under a rigorous DP-preservation across benchmark datasets compared with existing baselines. 
    </blockquote>
    <script>
        $("#spot-19").click(function(){
            $("#abstract-19").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Privacy Vulnerabilities in Marginals-based Synthetic Data</em> <br> 
    Steven&nbsp;Golob, Sikha&nbsp;Pentyala, Anuar&nbsp;Maratkhan, Martine&nbsp;De Cock (University&nbsp;of&nbsp;Washington&nbsp;Tacoma) <br>
    <div class='button-group'>
        <span class='button' id='spot-55'><small>📃</small> Abstract</span>  <a class='button' href='https://arxiv.org/abs/2410.05506'><small>📚</small> Arxiv</a> 
    </div>
    <blockquote class='paper-abstract' id='abstract-55'>
        When acting as a privacy-enhancing technology, synthetic data generation (SDG) aims to maintain a resemblance to the real data while excluding personally-identifiable information. Many SDG algorithms provide robust differential privacy (DP) guarantees to this end. However, we show that the strongest class of SDG algorithms–those that preserve marginal probabilities, or similar statistics, from the underlying data–leak information about individuals that can be recovered more efficiently than previously understood. We demonstrate this by presenting a novel membership inference attack, MAMA-MIA, and evaluate it against three seminal DP SDG algorithms: MST, PrivBayes, and Private-GSD. MAMA-MIA leverages knowledge of which SDG algorithm was used, allowing it to learn information about the hidden data more accurately, and orders-of-magnitude faster, than other leading attacks. We use MAMA-MIA to lend insight into existing SDG vulnerabilities. Our approach went on to win the first SNAKE (SaNitization Algorithm under attacK ... ε) competition. 
    </blockquote>
    <script>
        $("#spot-55").click(function(){
            $("#abstract-55").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Avoiding Pitfalls for Privacy Accounting of Subsampled Mechanisms under Composition</em> <br> 
    Christian Janos&nbsp;Lebeda (Inria), Matthew&nbsp;Regehr, Gautam&nbsp;Kamath (University&nbsp;of&nbsp;Waterloo), Thomas&nbsp;Steinke (Google&nbsp;DeepMind) <br>
    <div class='button-group'>
        <span class='button' id='spot-92'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-92'>
        We consider the problem of computing tight privacy guarantees for the composition of subsampled differentially private mechanisms. Recent algorithms can numerically compute the privacy parameters to arbitrary precision but must be carefully applied.  Our main contribution is to address two common points of confusion. First, some privacy accountants assume that the privacy guarantees for the composition of a subsampled mechanism are determined by self-composing the worst-case datasets for the uncomposed mechanism. We show that this is not true in general. Second, Poisson subsampling is sometimes assumed to have similar privacy guarantees compared to sampling without replacement. We show that the privacy guarantees may in fact differ significantly between the two sampling schemes. In particular, we give an example of hyperparameters that result in <em>ε ≈ 1</em> for Poisson subsampling and <em>ε > 10</em> for sampling without replacement. This occurs for some parameters that could realistically be chosen for DP-SGD. 
    </blockquote>
    <script>
        $("#spot-92").click(function(){
            $("#abstract-92").slideToggle("fast", "linear");
        });
    </script>
</li> <li class='paper-item program paper'>
    <em class='paper-title'>Auditing Differential Privacy Guarantees Using Density Estimation</em> <br> 
    Antti&nbsp;Koskela, Jafar&nbsp;Mohammadi (Nokia&nbsp;Bell&nbsp;Labs) <br>
    <div class='button-group'>
        <span class='button' id='spot-134'><small>📃</small> Abstract</span>   
    </div>
    <blockquote class='paper-abstract' id='abstract-134'>
        We present a novel method for accurately auditing the differential privacy (DP) guarantees of DP mechanisms. In particular, our solution is applicable to auditing DP guarantees of machine learning (ML) models. Previous auditing methods tightly capture the privacy guarantees of DP-SGD trained models in the white-box setting where the auditor has access to all intermediate models; however, the success of these methods depends on a priori information about the parametric form of the noise and the subsampling ratio used for sampling the gradients. We present a method that does not require such information and is agnostic to the randomization used for the underlying mechanism. Similarly to several previous DP auditing methods, we assume that the auditor has access to a set of independent observations from two one-dimensional distributions corresponding to outputs from two neighbouring datasets. Furthermore, our solution is based on a simple histogram-based density estimation technique to find lower bounds for the statistical distance between these distributions when measured using the hockey-stick divergence. We show that our approach also naturally generalizes the previously considered class of threshold membership inference auditing methods. We improve upon accurate auditing methods such as the f-DP auditing. Moreover, we address an open problem posed by Nasr et al. (2023) on how to accurately audit the subsampled Gaussian mechanism without any knowledge of the parameters of the underlying mechanism. 
    </blockquote>
    <script>
        $("#spot-134").click(function(){
            $("#abstract-134").slideToggle("fast", "linear");
        });
    </script>
</li> </ul>

<h5 class='closing'> <div class='slot-time'>16:40&ndash;17:00</div> <a class='anchor' name='04111640'></a> <div class='slot-title closing'>Closing Remarks</div>
</h5>
<br/><hr>