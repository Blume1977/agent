# Review comment examples

Worked comments for the visible text in [docs/a38.md](../docs/a38.md). The no-defect comments are complete declarations. `validate_visible` also accepts the non-blocking defect pair, but an accepted declaration still has `defects` 0, so that pair is shown without a machine block. Defects that block the merge have no completion comment. This file is not a second specification.

`EN:` comes first. Each label is its own line. Each language has a title and two sentences. A blank line separates the languages. The task sentence and the machine block stay in `<details>`.

The head below is a placeholder. Use the current 40-hex head. When the base revision has no `REVIEW.md`, the prompts are the two sentences shown. When it has `REVIEW.md`, each prompt is the compliance sentence from the specification.

## First review, no defects

This is the comment Ready reads. Post it only when that run found no defects. `N` is how many passes that took.

````
EN:
First review
Ready after 2 review passes.
The payment amount is checked against the invoice before it is sent.

DE:
Erster Review
Bereit nach 2 Review-Durchläufen.
Der Zahlungsbetrag wird vor dem Senden gegen die Rechnung geprüft.

<details>
<summary>Details</summary>

Head: `0123456789abcdef0123456789abcdef01234567`
Runs: `conformity-a` with `logic-a`.
Lane `conformity-a`:
Provider: Acme
Model: Acme model
Model number: acme-1
Result: pass
Prompt:
```text
Review the complete PR diff for conformity with CONTRIBUTING.md.
```
Lane `logic-a`:
Provider: Acme
Model: Acme model
Model number: acme-1
Result: pass
Prompt:
```text
Review the complete PR diff for logical correctness.
```
Final result: `passes` 2, `defects` 0.
Set aside: none.

<!-- A38-REVIEW:v1 -->
```json
{"schema":"a38-review/v2","head":"0123456789abcdef0123456789abcdef01234567","passes":2,"defects":0,"set_aside":"none","lanes":[{"id":"conformity-a","result":"pass","status":"complete","provider":"Acme","model":"Acme model","model_number":"acme-1","prompt":"Review the complete PR diff for conformity with CONTRIBUTING.md."},{"id":"logic-a","result":"pass","status":"complete","provider":"Acme","model":"Acme model","model_number":"acme-1","prompt":"Review the complete PR diff for logical correctness."}]}
```
<!-- /A38-REVIEW:v1 -->

</details>
````

## Second review, no defects

A later comment. It does not satisfy Ready. The two sentences are this pair and no others. The sentence about what the pull request changes stays in the details.

````
EN:
Second review
No defects.
Nothing in this review blocks the merge.

DE:
Zweiter Review
Keine Mängel.
Nichts aus diesem Review blockiert den Merge.

<details>
<summary>Details</summary>

The payment amount is checked against the invoice before it is sent.

Der Zahlungsbetrag wird vor dem Senden gegen die Rechnung geprüft.

Head: `0123456789abcdef0123456789abcdef01234567`
Runs: `conformity-b` with `logic-b`. The second run may be omitted.
Lane `conformity-b`:
Provider: Acme
Model: Acme model
Model number: acme-1
Result: pass
Prompt:
```text
Review the complete PR diff for conformity with CONTRIBUTING.md.
```
Lane `logic-b`:
Provider: Acme
Model: Acme model
Model number: acme-1
Result: pass
Prompt:
```text
Review the complete PR diff for logical correctness.
```
Final result: `passes` 1, `defects` 0.
Set aside: none.

<!-- A38-REVIEW:v1 -->
```json
{"schema":"a38-review/v2","head":"0123456789abcdef0123456789abcdef01234567","passes":1,"defects":0,"set_aside":"none","lanes":[{"id":"conformity-b","result":"pass","status":"complete","provider":"Acme","model":"Acme model","model_number":"acme-1","prompt":"Review the complete PR diff for conformity with CONTRIBUTING.md."},{"id":"logic-b","result":"pass","status":"complete","provider":"Acme","model":"Acme model","model_number":"acme-1","prompt":"Review the complete PR diff for logical correctness."}]}
```
<!-- /A38-REVIEW:v1 -->

</details>
````

## Second review, defects that do not block the merge

The visible pair says that this review found defects and that they do not block the merge. Each defect is named in the details. The first review stays in place. This comment does not return the pull request to draft, and it does not satisfy Ready.

An accepted declaration still has `defects` 0. Do not put that machine block under these lines: the visible text would contradict it. A machine block with `defects` greater than 0 is rejected with `review defects must be 0`.

```
EN:
Second review
There are defects.
They do not block the merge.

DE:
Zweiter Review
Es gibt Mängel.
Sie blockieren den Merge nicht.

<details>
<summary>Details</summary>

The amount is taken from the request, so the caller can underpay. This does not block the merge.

Der Betrag kommt aus dem Request, der Aufrufer kann zu wenig zahlen. Das blockiert den Merge nicht.

</details>
```

## Blocking defects

There is no completion comment for defects that block the merge. The second review has no such pair. The first review is posted only after that run has no defects left.

Until then the review states the defects, and nothing else is posted as the review comment:

```
FINDINGS:
1. src/pay.ts:40 — the amount is taken from the request, so the caller can underpay.
```

After the fix, post the [first review](#first-review-no-defects). `N` is the number of passes until no defects remained.

## Not this

The pass-count lines are not the second review. Neither is a mixed pair.

```
EN:
Second review
Second review after 1 review passes.
No defects, and nothing in this review blocks the merge.
```
