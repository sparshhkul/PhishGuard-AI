// ======================================
// ROTATING TEXT
// ======================================

const words = document.querySelectorAll(".rotating-word");

if (words.length) {

    let current = 0;

    setInterval(() => {

        words[current].classList.remove("active");
        words[current].classList.add("exit");

        current = (current + 1) % words.length;

        words[current].classList.remove("exit");
        words[current].classList.add("active");

    }, 2500);

}


// ======================================
// BACKGROUND
// ======================================

const background = document.querySelector(".background");

if (background) {

    let pos = 0;

    setInterval(() => {

        pos++;

        background.style.backgroundPosition =
            `${pos}px ${pos}px, ${-pos}px ${-pos}px`;

    }, 80);

}


// ======================================
// UNIVERSAL SCANNER
// ======================================

function startScan(type){

    document.getElementById("loadingOverlay").style.display="flex";

    const progressBar=document.getElementById("progressBar");
    const progressPercent=document.getElementById("progressPercent");
    const loaderText=document.getElementById("loaderText");

    const step1=document.getElementById("step1");
    const step2=document.getElementById("step2");
    const step3=document.getElementById("step3");
    const step4=document.getElementById("step4");
    const step5=document.getElementById("step5");

    let messages=[];

    if(type==="email"){

        messages=[
            "Parsing Email...",
            "Checking Keywords...",
            "Inspecting Embedded URLs...",
            "Running AI Detection...",
            "Generating Report..."
        ];

    }

    if(type==="url"){

        messages=[
            "Reading URL...",
            "Checking Domain...",
            "Scanning Reputation...",
            "Running AI Detection...",
            "Generating Report..."
        ];

    }

    if(type==="sms"){

        messages=[
            "Reading SMS...",
            "Finding Scam Keywords...",
            "Intent Analysis...",
            "Running AI Detection...",
            "Generating Report..."
        ];

    }

    const steps=[step1,step2,step3,step4,step5];

    loaderText.innerHTML=messages[0];

    let progress=0;
    let currentStep=0;

    steps[0].classList.add("active");

    const timer=setInterval(()=>{

        progress++;

        progressBar.style.width=progress+"%";
        progressPercent.innerHTML=progress+"%";

        if(progress%20===0 && currentStep<4){

            steps[currentStep].classList.remove("active");
            steps[currentStep].classList.add("done");

            currentStep++;

            steps[currentStep].classList.add("active");

            loaderText.innerHTML=messages[currentStep];

        }

        if(progress>=100){

            clearInterval(timer);

        }

    },40);

}


// ======================================
// EMAIL
// ======================================

const emailBtn = document.getElementById("scanBtn");

if (emailBtn) {

    emailBtn.onclick = function () {

        const email = document.getElementById("emailInput").value.trim();

        if (email === "") {
            alert("Please paste an email.");
            return;
        }

        startScan("email");

        setTimeout(() => {

            document.getElementById("emailForm").submit();

        }, 3500);

    };

}


// ======================================
// URL
// ======================================

const urlBtn = document.getElementById("scanUrlBtn");

if (urlBtn) {

    urlBtn.onclick = function () {

        const value = document.getElementById("urlInput").value.trim();

        if (value === "") {
            alert("Please paste a URL.");
            return;
        }

        startScan("url");

        setTimeout(() => {

            document.getElementById("loadingOverlay").style.display = "none";

            window.location.href = "/result-demo-url";

        }, 4200);

    };

}


// ======================================
// SMS
// ======================================

const smsBtn = document.getElementById("scanSmsBtn");

if (smsBtn) {

    smsBtn.onclick = function () {

        const value = document.getElementById("smsInput").value.trim();

        if (value === "") {
            alert("Please paste an SMS.");
            return;
        }

        startScan("sms");

        setTimeout(() => {

            document.getElementById("loadingOverlay").style.display = "none";

            window.location.href = "/result-demo-sms";

        }, 4200);

    };

}