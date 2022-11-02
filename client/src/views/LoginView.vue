<template>
    <div class="wrapper">
        <div>
            <form @submit.prevent="submitForm">
                <div class="mb-3">
                    <label for="usernameInput" class="form-label">Username</label>
                    <input v-model="authCredentials.username" class="form-control" id="usernameInput" />
                </div>
                <div class="mb-3">
                    <label for="passwordInput" class="form-label">Password</label>
                    <input v-model="authCredentials.password" class="form-control" id="passwordInput" />
                </div>
                <button type="submit" class="btn btn-success" >Sign in</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue"
import { useAuthStore } from "../stores/auth"

const authStore = useAuthStore()

const authCredentials = ref({
    username: "",
    password: ""
})

const submitForm = () => {
    authStore.login(authCredentials.value)
}

</script> 

<style scoped>
.wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

.form-control:focus {
    /* border-color; */
    box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
}
</style>
