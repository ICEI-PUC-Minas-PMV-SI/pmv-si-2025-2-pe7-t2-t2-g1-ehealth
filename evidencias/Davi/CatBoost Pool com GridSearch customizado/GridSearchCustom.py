depths = [5, 7, 9]
learning_rates = [0.03, 0.05, 0.087]
iterations_list = [200, 500, 700]
loss_functions = ["Logloss", "MultiClass"]
custom_metric = ["AUC", "Accuracy", "F1", "Recall"]

results = []

for depth in depths:
    for lr in learning_rates:
        for iters in iterations_list:
            for loss_fn in loss_functions:

                print(
                    f"\n============================="
                    f"\nTestando: depth={depth}, lr={lr}, iters={iters}, loss={loss_fn}"
                    f"\n============================="
                )
                model = CatBoostClassifier(
                    depth=depth,
                    learning_rate=lr,
                    iterations=iters,
                    loss_function=loss_fn,
                    eval_metric="AUC",
                    custom_metric=custom_metric,
                    auto_class_weights="Balanced",
                    random_seed=42,
                    verbose=0
                )
                model.fit(
                    train_pool,
                    eval_set=test_pool,
                    use_best_model=True
                )
                y_pred = model.predict(X_test)
                y_proba = model.predict_proba(X_test)[:, 1]
                report = classification_report(
                    y_test,
                    y_pred,
                    zero_division=0,
                    digits=5
                )
                auc = roc_auc_score(y_test, y_proba)

                print(f"AUC (teste): {auc:.5f}")
                print("\nRelatório de Classificação:\n", report)
                results.append({
                    "depth": depth,
                    "learning_rate": lr,
                    "iterations": iters,
                    "loss_function": loss_fn,
                    "custom_metric": custom_metric,
                    "auc_test": auc,
                    "report": report
                })
best_run = max(results, key=lambda x: x["auc_test"])

print("\n\n===== MELHOR COMBINAÇÃO ENCONTRADA =====")
print(f"depth        : {best_run['depth']}")
print(f"learning_rate: {best_run['learning_rate']}")
print(f"iterations   : {best_run['iterations']}")
print(f"loss_function: {best_run['loss_function']}")
print(f"custom_metric: {best_run['custom_metric']}")
print(f"AUC (teste)  : {best_run['auc_test']:.5f}")

print("\nRelatório de Classificação da melhor combinação:\n")
print(best_run["report"])